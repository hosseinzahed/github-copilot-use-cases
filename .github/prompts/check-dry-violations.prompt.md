---
agent: 'agent'
description: 'Check DRY'
tools: ['edit/editFiles', 'search', 'vscode/newWorkspace', 'execute/runInTerminal', 'vscode/runCommand', 'search/usages', 'vscode/vscodeAPI', 'read/problems', 'search/changes', 'execute/testFailure', 'vscode/openSimpleBrowser', 'web/fetch', 'web/githubRepo', 'vscode/extensions', 'execute/runTests']
---

# 🔍 DRY Violation Analysis & Refactoring Recommendations

## 🎯 Objective
Analyze the codebase for DRY (Don't Repeat Yourself) violations and provide actionable refactoring recommendations to improve code maintainability, reduce duplication, and enhance overall code quality.

## 🔎 Areas to Analyze

### 1. **API Patterns** 🛣️
Examine all REST controller files in `src/main/java/com/example/pe/` for:
- **CRUD Operations**: Identical GET, POST, PUT, DELETE patterns
- **Swagger Documentation**: Repetitive OpenAPI schema definitions
- **Error Handling**: Duplicate 404/400/500 error responses
- **Validation Logic**: Similar input validation patterns
- **Response Formatting**: Repeated JSON response structures

### 2. **Business Logic** 💼
Check for duplicated business logic in:
- **Model Definitions**: Similar interfaces and types
- **Data Transformation**: Repeated mapping/formatting functions
- **Validation Rules**: Duplicate validation logic
- **Utility Functions**: Similar helper functions

### 3. **Configuration & Setup** ⚙️
Look for configuration duplication in:
- **Environment Variables**: Repeated config patterns

## 📊 Analysis Framework

### **Severity Levels**
- 🔴 **Critical**: Extensive duplication (>5 instances)
- 🟡 **Moderate**: Notable duplication (3-5 instances)
- 🟢 **Minor**: Limited duplication (2-3 instances)

### **Refactoring Impact**
- ⚡ **High Impact**: Affects multiple files/modules
- 📈 **Medium Impact**: Affects single module/feature
- 🔧 **Low Impact**: Localized improvements

## 🛠️ Recommended Refactoring Patterns

### **For API Routes:**
1. **Generic CRUD Controller**: Create base controller class
2. **Response Helpers**: Centralize response formatting
3. **Validation Decorators**: Reusable validation logic

### **For Business Logic:**
1. **Service Layer**: Centralize business operations
2. **Factory Patterns**: Create object instances consistently
3. **Strategy Pattern**: Handle similar operations differently
4. **Utility Modules**: Group related helper functions

## 📝 Deliverables

### **1. Violation Report**
Create a detailed report containing:
- **File-by-file analysis** of duplication found
- **Code snippets** showing exact duplicated patterns
- **Severity assessment** using the framework above
- **Quantified metrics** (lines duplicated, files affected)

### **2. Refactoring Plan**
Provide a prioritized action plan with:
- **Quick Wins**: Easy refactoring opportunities (< 2 hours)
- **Medium Efforts**: Moderate refactoring tasks (2-8 hours)
- **Large Projects**: Comprehensive restructuring (> 8 hours)

### **3. Implementation Suggestions**
For each violation, provide:
- **Before/After Code Examples**: Show current vs. refactored code
- **Migration Steps**: Step-by-step refactoring instructions
- **Testing Strategy**: How to validate refactoring doesn't break functionality
- **Performance Impact**: Expected improvements in bundle size, maintainability

## 🎯 Success Criteria

- [ ] **Comprehensive Analysis**: All major code duplication identified
- [ ] **Actionable Recommendations**: Clear, implementable suggestions
- [ ] **Prioritized Backlog**: Tasks ranked by impact vs. effort
- [ ] **Code Examples**: Concrete before/after demonstrations
- [ ] **Metrics**: Quantified improvement estimates

## 🚀 Getting Started

1. **Scan REST Controller Files**: Start with `src/main/java/com/example/pe/` directory
2. **Analyze Patterns**: Look for identical or nearly identical code blocks
3. **Document Findings**: Create violation inventory with severity ratings
4. **Propose Solutions**: Design generic abstractions and patterns
5. **Create Examples**: Show practical refactoring implementations

## 📚 Focus Areas for This Codebase

Based on the architecture:

### **High-Priority Targets:**
- **REST API Routes**: REST controller files with identical CRUD patterns
- **Swagger Documentation**: Repetitive OpenAPI schema definitions
- **Error Handling**: Duplicate 404/error responses across routes
- **Entity Models**: Similar TypeScript interfaces

### **Secondary Targets:**
- **Testing Patterns**: Similar test structures across files
