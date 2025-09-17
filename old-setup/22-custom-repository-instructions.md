### Adding repository custom instructions for GitHub Copilot

GitHub Copilot can provide chat responses that are tailored to the way your team works, 
the tools you use, or the specifics of your project, if you provide it with enough context to do so. 
Instead of repeatedly adding this contextual detail to your chat questions, 
you can create files in your repository that automatically add this information for you.

There are two types of files you can use to provide context and instructions to GitHub Copilot Chat in VS Code:

- **Repository** custom instructions allow you to specify repository-wide instructions and preferences, in a single file, that apply to any conversation held in the context of the repository.
- **Prompt** files (public preview) allow you to save common prompt instructions and relevant context in Markdown files (*.prompt.md) that you can then reuse in your chat prompts. Prompt files are only available in VS Code.

*Example: .github/copilot-instructions.md file contains three instructions that will be added to all chat questions.*
```
We use .NET for our development and manage our dependencies with NuGet.

We always write TypeScript with double quotes and tabs for indentation,
so when your responses include TypeScript code, please follow those conventions.

Our team uses GitHub Projects for tracking items of work.
```

[Read more](https://docs.github.com/en/enterprise-cloud@latest/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=vscode)
