# Contributing to the eVote System

Thank you for taking the time to contribute to our eVote System project! The following guidelines will help you understand how to contribute effectively and ensure our collaboration runs smoothly.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
3. [Reporting Issues](#reporting-issues)
4. [Branching Strategy](#branching-strategy)
5. [Coding Guidelines](#coding-guidelines)
6. [Submitting a Pull Request](#submitting-a-pull-request)
7. [Code Review Process](#code-review-process)
8. [Testing](#testing)
9. [Communication](#communication)

---

## Project Overview

The **eVote System** is being developed to provide a secure, user-friendly, and scalable electronic voting platform. It aims to support elections in various contexts, ensuring transparency, privacy, and ease of use.

We welcome contributions that:
- Enhance security (e.g., authentication, encryption)
- Improve the user interface and user experience
- Add new features
- Fix bugs
- Improve performance or scalability

---

## Getting Started

### Prerequisites
Before contributing, ensure you have the following installed:
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/) and Flask (if working on the backend)
- Frontend tools (e.g., html,css, Bootstrap5) if working on the frontend
- [Docker](https://www.docker.com/) (optional, for containerized deployment)

### Fork the Repository
1. Fork the [eVote System repository](https://github.com/KyucsaDevs/eVote) to your GitHub account.
2. Clone the forked repository to your local machine:
   ```bash
   git clone https://https://github.com/KyucsaDevs/eVote.git
   ```

3. Navigate to the project directory:
   ```
   cd eVote
   ```

4. Set up the project dependencies:
     ```
     pip install -r requirements.txt
     ```
---

## Reporting Issues

If you encounter any bugs, security vulnerabilities, or want to request a feature:
1. Check if an issue already exists in the [Issues](https://github.com/KyucsaDevs/eVote/issues) section.
2. If not, create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce the issue (if it's a bug)
   - Expected vs actual behavior
   - Relevant screenshots, logs, or error messages

---

## Branching Strategy

We follow the **Git Flow** branching model:
1. **`main`**: This branch contains the production-ready code.
2. **`develop`**: This branch contains the latest development code, and all new features should branch off from here.
3. **Feature branches** (`feature/your-feature-name`): Used for developing new features or fixing bugs.
4. **Bugfix branches** (`bugfix/issue-number`): Used to address specific bugs.

### Branch Naming Convention
- Use lowercase and hyphens to separate words.
- Examples:
  - `feature/user-authentication`
  - `bugfix/fix-issue-123`

---

## Coding Guidelines

Please follow these coding standards to maintain consistency:

### Backend (Python, Flask)
- Follow [PEP 8](https://pep8.org/) for Python code.
- Use meaningful variable names and comments.
- For database models, ensure field validation and constraints are enforced at both the model and database level.

### General Guidelines
- Avoid code duplication and ensure your code is DRY (Don't Repeat Yourself).
- Break large functions or components into smaller, manageable ones.
- Write unit tests for new features or changes.

---

## Submitting a Pull Request

Once your changes are complete:
1. Push your changes to your branch:
   ```
   git push origin feature/your-feature-name
   ```
   
2. Create a pull request (PR) on the repository's GitHub page.
3. Follow the PR template to provide:
   - A clear description of what the PR addresses
   - Screenshots or GIFs of the changes, if applicable
   - A list of issues fixed (if any)

Ensure that:
- Your PR is up-to-date with the `develop` branch.
- All tests pass locally.

---

## Code Review Process

Once you submit a pull request:
- A project maintainer will review your code.
- You may be asked to make changes based on feedback.
- When approved, the PR will be merged into the `develop` branch.
- If you are a maintainer, ensure to wait for at least one review from another team member before merging.

---

## Testing

Ensure that your code is fully tested. This includes:
- Unit tests for individual functions or components.
- Integration tests for ensuring components work together as expected.
- Running the full test suite before submitting a PR.

Use the following commands to run the project:
- **Backend (Flask)**: 
  ```
  python run.py
  ```

---

## Communication

For any questions or discussions:
- Use the project’s Slack channel for real-time communication.
- You can also reach out via the [Discussions](https://github.com/KyucsaDevs/eVote/discussions) section on GitHub for general topics.

---

We appreciate your time and contributions in making the eVote System a success!

---