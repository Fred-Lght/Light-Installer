# Light Installer

Light Installer is a **light**weight operating system installation interface designed to simplify and streamline the OS installation process. It is built with Python and Qt, focusing on clarity, minimal overhead, and a smooth user experience.

Features
* Simple and structured installation flow
* Qt-based graphical interface
* Modular design for extending installation steps
* Cross-platform Python-based implementation (depending on backend support)
* Designed with clarity and maintainability in mind
* Design Philosophy

Light Installer is built around the idea that system installation tools should not feel heavy or complicated. It aims to reduce friction in setup workflows while keeping the architecture open for future expansion into more advanced tooling.


## Roadmap
#### Phase 1: Core Application (Python + Qt)
* Stabilize UI and installation workflow
* Define modular step system for installation stages
* Improve error handling and logging system
* Separate core logic from UI layer
#### Phase 2: Architecture Refactoring
* Extract core logic into a reusable backend layer
* Introduce plugin-based system for installation modules
* Improve configuration management
#### Phase 3: Framework Transition (C++)
* Rewrite core backend as a C++ framework
* Expose stable API for external tools and installers
* Focus on performance and system-level integration
Phase 4: Lua Configuration Layer
Introduce Lua-based configuration system
Allow scripting of installation flows and modules
Enable user-defined installation profiles
Phase 5: Ecosystem Expansion
Create reusable framework for custom OS installers
Improve documentation and developer tooling
Provide bindings between Python, C++, and Lua layers
Future Direction

The long-term goal is to evolve Light Installer from a standalone Python application into a modular installation framework. This framework will support multiple frontends, a performant C++ core, and flexible Lua-based configuration for customization.
