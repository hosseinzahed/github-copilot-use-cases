using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Text.Json;

namespace StockPriceChecker
{
    class Program
    {
        // Entry point of the application
        static async Task Main(string[] args)
        {
            // Stock symbol to fetch (MSFT for Microsoft)
            string stockSymbol = "MSFT";
            
            Console.WriteLine($"Fetching stock price for {stockSymbol}...\n");
            
            try
            {
                // Fetch the stock price from Yahoo Finance API
                var stockPrice = await GetStockPriceAsync(stockSymbol);
                
                // Display the results
                Console.WriteLine($"Stock Symbol: {stockPrice.Symbol}");
                Console.WriteLine($"Current Price: ${stockPrice.RegularMarketPrice:F2}");
                Console.WriteLine($"Previous Close: ${stockPrice.RegularMarketPreviousClose:F2}");
                Console.WriteLine($"Market Change: ${stockPrice.RegularMarketChange:F2} ({stockPrice.RegularMarketChangePercent:F2}%)");
                Console.WriteLine($"Day High: ${stockPrice.RegularMarketDayHigh:F2}");
                Console.WriteLine($"Day Low: ${stockPrice.RegularMarketDayLow:F2}");
                Console.WriteLine($"Volume: {stockPrice.RegularMarketVolume:N0}");
            }
            catch (Exception ex)
            {
                // Handle any errors that occur during the API call
                Console.WriteLine($"Error fetching stock price: {ex.Message}");
            }
            
            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
        
        /// <summary>
        /// Fetches stock price data from Yahoo Finance API
        /// </summary>
        /// <param name="symbol">The stock symbol to fetch (e.g., "MSFT")</param>
        /// <returns>A StockData object containing the stock information</returns>
        static async Task<StockData> GetStockPriceAsync(string symbol)
        {
            // Create an HTTP client to make the API request
            using (var client = new HttpClient())
            {
                // Set a user agent to avoid being blocked by Yahoo Finance
                client.DefaultRequestHeaders.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36");
                
                // Construct the Yahoo Finance API URL
                // This uses the query1 API endpoint which provides real-time stock data
                string apiUrl = $"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d";
                
                // Make the HTTP GET request
                var response = await client.GetAsync(apiUrl);
                
                // Ensure the request was successful
                response.EnsureSuccessStatusCode();
                
                // Read the response content as a string
                var jsonResponse = await response.Content.ReadAsStringAsync();
                
                // Parse the JSON response
                using (JsonDocument doc = JsonDocument.Parse(jsonResponse))
                {
                    // Navigate through the JSON structure to extract the stock data
                    var result = doc.RootElement
                        .GetProperty("chart")
                        .GetProperty("result")[0];
                    
                    var meta = result.GetProperty("meta");
                    
                    // Helper method to safely get double values with fallback
                    double GetDoubleOrDefault(JsonElement element, string propertyName, double defaultValue = 0)
                    {
                        if (element.TryGetProperty(propertyName, out JsonElement prop))
                        {
                            if (prop.ValueKind == JsonValueKind.Number)
                                return prop.GetDouble();
                        }
                        return defaultValue;
                    }
                    
                    // Helper method to safely get long values with fallback
                    long GetLongOrDefault(JsonElement element, string propertyName, long defaultValue = 0)
                    {
                        if (element.TryGetProperty(propertyName, out JsonElement prop))
                        {
                            if (prop.ValueKind == JsonValueKind.Number)
                                return prop.GetInt64();
                        }
                        return defaultValue;
                    }
                    
                    // Extract the relevant stock price information with safe parsing
                    var symbol_value = meta.GetProperty("symbol").GetString();
                    var currentPrice = GetDoubleOrDefault(meta, "regularMarketPrice");
                    var previousClose = GetDoubleOrDefault(meta, "previousClose");
                    var dayHigh = GetDoubleOrDefault(meta, "regularMarketDayHigh");
                    var dayLow = GetDoubleOrDefault(meta, "regularMarketDayLow");
                    var volume = GetLongOrDefault(meta, "regularMarketVolume");
                    
                    // Calculate the change and percentage change
                    var change = currentPrice - previousClose;
                    var changePercent = previousClose > 0 ? (change / previousClose) * 100 : 0;
                    
                    return new StockData
                    {
                        Symbol = symbol_value,
                        RegularMarketPrice = currentPrice,
                        RegularMarketPreviousClose = previousClose,
                        RegularMarketChange = change,
                        RegularMarketChangePercent = changePercent,
                        RegularMarketDayHigh = dayHigh,
                        RegularMarketDayLow = dayLow,
                        RegularMarketVolume = volume
                    };
                }
            }
        }
    }
    
    /// <summary>
    /// Data model to hold stock price information
    /// </summary>
    class StockData
    {
        // The stock symbol (e.g., "MSFT")
        public string Symbol { get; set; }
        
        // The current market price of the stock
        public double RegularMarketPrice { get; set; }
        
        // The previous closing price
        public double RegularMarketPreviousClose { get; set; }
        
        // The change in price from the previous close
        public double RegularMarketChange { get; set; }
        
        // The percentage change from the previous close
        public double RegularMarketChangePercent { get; set; }
        
        // The highest price during the trading day
        public double RegularMarketDayHigh { get; set; }
        
        // The lowest price during the trading day
        public double RegularMarketDayLow { get; set; }
        
        // The trading volume for the day
        public long RegularMarketVolume { get; set; }
    }
}
