## GitHub Copilot Instructions:

GitHub Copilot instructions allow you to customize how the AI generates code and handles development tasks by providing specific guidelines and rules.

### Types of Instructions:

- **Repository-wide Instructions:** These are specified in a .github/copilot-instructions.md file located in the root of your repository. They apply to all requests made in the context of that repository, providing general guidance on coding standards and practices.
- **Path-specific Instructions:** These instructions are defined in one or more .instructions.md files within the .github/instructions directory. They apply to requests made in the context of files that match specified paths, allowing for more granular control over how Copilot behaves with different parts of your project.
- **Agent Instructions:** These are used by AI agents and can be stored in AGENTS.md files located anywhere within the repository. The nearest AGENTS.md file in the directory tree will take precedence when Copilot is working.

### Creating Custom Instructions

- **Define Your Instructions:** You can create a custom instructions file from scratch or ask Copilot to generate one for you. The instructions should be written in Markdown format and can include guidelines for coding practices, project requirements, and specific contexts.
- **Use Markdown Links:** To reference specific context in your instructions, such as files or URLs, you can use Markdown links. This helps keep your instructions organized and focused.
- **Enable Custom Instructions:** Ensure that the custom instructions feature is enabled in your GitHub settings. This is typically enabled by default.

### Best Practices

- **Keep Instructions Clear and Concise:** Each instruction should be a single, simple statement. If you have multiple pieces of information, use multiple instructions to maintain clarity.
- **Organize Instructions by Context:** Use different instruction files for various programming languages, frameworks, or project types. This helps ensure that the right instructions are applied to the appropriate files.
- **Collaborate with Team Members:** Store project-specific instructions in your workspace to share them with other team members and include them in version control. This promotes consistency across the project.
  By utilizing GitHub Copilot instructions effectively, you can enhance the AI's ability to generate code that aligns with your project's standards and requirements, ultimately improving your development workflow.

### Sources
- [https://github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)
- [https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
- [https://code.visualstudio.com/docs/copilot/customization/custom-instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [https://github.blog/changelog/2025-08-06-copilot-coding-agent-automatically-generate-custom-instructions/](https://github.blog/changelog/2025-08-06-copilot-coding-agent-automatically-generate-custom-instructions/)
- [https://devblogs.microsoft.com/dotnet/prompt-files-and-instructions-files-explained/](https://devblogs.microsoft.com/dotnet/prompt-files-and-instructions-files-explained/)
