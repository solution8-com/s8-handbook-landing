# Standards

Coding conventions, review rules, and quality checks.

**See also:** [Tech Stack](../tech-stack/README.md) · [Tools & Utils](../tech-stack/tools-utils.md) · [Templates](../tech-stack/templates.md) · [Dev Lifecycle](lifecycle.md)


#### Best Practices for Writing Maintainable Code

Maintaining clean, adaptable, and secure code is fundamental for long-term peace-of-mind. These practices help ensure your codebase remains manageable while accommodating future needs.

## Software Maintainability Standards

#### Definition

Maintainability is the ease with which a software system can be modified, updated, extended, or repaired over time. It impacts the long-term viability and sustainability of a software system. A maintainable system is one that is easy to understand, has clear and modular code, is well-documented, and has a low risk of introducing errors when changes are made.

---

#### Characteristics

| Characteristic | Description |
| :-- | :-- |
| **Modularity** | The software is divided into discrete, independent modules or components, each with a clear and specific functionality. This makes it easier to modify or replace individual parts without affecting the entire system. |
| **Readability** | Code is written clearly and concisely, following consistent naming conventions, coding standards, and documentation practices. Readable code is easier for developers to understand, troubleshoot, and enhance. |
| **Testability** | The software is designed to support thorough testing, with components that can be tested independently. This includes unit tests, integration tests, and automated testing frameworks that facilitate ongoing validation of the software's behaviour. |
| **Documentation** | Comprehensive and up-to-date documentation is provided, including docstrings, design documents, user manuals, and API references. Good documentation helps developers understand the system's structure, functionality, and dependencies. |
| **Simplicity** | The design and implementation of the software are kept as simple as possible, avoiding unnecessary complexity. Simple systems are easier to understand, maintain, and extend. |
| **Consistency** | Consistent use of design patterns, coding practices, language best practices, and architectural principles throughout the software. Consistency reduces the learning curve for new developers and helps maintain uniform quality across the codebase. |
| **Configurability** | The software allows configuration through external files or settings rather than hard-coded values. This makes it easier to adapt the software to different environments or requirements without changing the code. |
| **Dependency Management** | Proper management of dependencies ensures that external libraries or components can be updated or replaced without major disruptions. This includes using dependency injection, version control, and modular design. Version management for your own code ensures consistent and reliable releases. |
| **Error Handling & Logging** | Robust error handling and logging mechanisms are in place to facilitate debugging and maintenance. This includes meaningful error messages, exception handling, and comprehensive logging of system events and errors. |

---

#### Best Practices for Writing Maintainable Code

###### Write Clean and Simple Code

Simplicity should always be a priority. Over-complicating solutions can lead to confusion and difficulty in troubleshooting. Focus on writing code that is intuitive and easy to follow. Use meaningful variable names, avoid deeply nested structures, and break down complex tasks into smaller, reusable functions or methods. Clean code ensures clarity for current and future developers.

###### Consistency in Code Structure

Consistency ensures that code follows the same style, making it easier for developers to read, understand, and work with. Naming variables and functions clearly, using consistent indentation, and following a standard formatting style are key aspects of maintaining consistency.

- **Good:** `user_name` — clearly identifies the purpose of the variable
- **Bad:** `x` — the meaning of the variable is unclear, leading to confusion

###### Readability is the True Indicator of Quality

Readable code is maintainable code. Complex, convoluted solutions may seem clever, but they are the enemy of efficiency. Variables have meaningful names, methods are concise, and tasks are broken into manageable units. Where complexity is unavoidable, comments explain intent, not implementation. Readable code reduces errors, accelerates onboarding, and ensures that projects remain viable in the long run.

Use single-purpose functions to improve both readability and maintainability:

```python
## Clear and focused
def calculate_area(length, width):
    return length * width
```

###### Follow the DRY (Don't Repeat Yourself) Principle

Redundancy in code increases the risk of inconsistencies and makes updates more tedious. Reuse functions, classes, or modules wherever possible. For example, shared utility functions can replace repeated logic across different parts of the application. Balance is key — over-abstraction can make code harder to read and understand.

###### Adhere to the SOLID Principles

The SOLID principles are object-oriented design guidelines that enhance code flexibility and scalability:

- **Single Responsibility:** Classes should focus on a single purpose.
- **Open/Closed:** Systems should be open to extension but closed to modification.
- **Liskov Substitution:** Code should allow substituting a subclass without affecting the program.
- **Interface Segregation:** Avoid forcing classes to implement unused features.
- **Dependency Inversion:** High-level logic and low-level details should both rely on abstractions.

###### Refactor and Optimize Regularly

Code is rarely written perfectly the first time. Regular refactoring keeps technical debt to a minimum, keeps code efficient and flexible, and allows it to change with evolving requirements. Teams that refactor consistently avoid code bloat and tangling, and create a foundation for sustainable development.

###### Unit Testing and Test-Driven Development (TDD)

Testing is not just about finding bugs — it is about building confidence in your code. Unit tests verify the behaviour of individual components, while TDD encourages writing tests before implementation, fostering a thoughtful approach to design. Regular testing throughout development ensures reliability and reduces the risk of introducing errors as the codebase evolves.

###### Regular Code Reviews

Peer reviews are invaluable for maintaining high standards. In the age of AI, this practice moves to the background. Beyond improving the code, reviews promote shared knowledge and learning among team members. When done consistently, they become a cornerstone of collaborative development. We use AI to enhance and accelerate this instead of replacing it. 

###### Prioritise Security

Security is integral to writing reliable software. Validating user inputs, sanitising data, and staying up to date with dependency patches help prevent vulnerabilities. Secure coding practices ensure that your software is not only functional but also trustworthy. 

###### Version Control as a Core Practice

Version control provides a reliable history of changes, safeguards collaboration, and prevents catastrophic errors. Write clear, meaningful commit messages, use branching to isolate features or fixes, and commit changes frequently to maintain a clean development history.

###### The CI/CD Discipline

Continuous Integration and Continuous Deployment (CI/CD) bring order and precision to software development. CI detects integration errors early, reducing the cost of fixing them. CD automates delivery, keeping the codebase in a deployable state at all times. Teams that adopt CI/CD workflows benefit from fewer bottlenecks, faster iteration, and greater confidence in their releases.

---

#### Implementations

| Practice | Detail |
| :-- | :-- |
| **Consistent Naming Conventions** | Use meaningful and consistent names for variables, functions, classes, and other entities. |
| **Code Formatting** | Follow consistent code formatting rules to enhance readability. AI coding agents effectively embody this and hardly ever require manual correction. |
| **Code Reviews** | In 2026, strict branch discipline and agentic code reviews are expected to ensure the software we deploy is safe and does not contain bugs that are security and stability-related. |
| **External Documentation** | The best way to document is to use Devin DeepWiki. |
| **README Files** | Provide README files in repositories to guide developers on setup, usage, and contribution guidelines. |
| **Automated Testing** | Provide unit tests, end-to-end tests, smoke tests, and integration tests as well as continuous integration practices. |
| **Code Refactoring** | Regularly refactor code to improve its structure, readability, and maintainability without changing its external behaviour. |

###### Readability is the True Indicator of Quality

Readable code is maintainable code. Complex, convoluted solutions may seem clever, but they are the enemy of efficiency. Teams that prioritize readability write code that is logical, structured, and easy to follow.

Variables have meaningful names, methods are concise, and tasks are broken into manageable units. Where complexity is unavoidable, comments explain intent, not implementation. Readable code reduces errors, accelerates onboarding, and ensures that projects remain viable in the long run.