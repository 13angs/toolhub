import typer
from rich.console import Console
import os
import importlib

# --- Application Setup ---
main_app = typer.Typer(
    name="toolhub",
    help="A collection of useful command-line tools.",
    rich_markup_mode="markdown"
)
console = Console()

# --- Dynamic Command Loading ---
def register_commands():
    """
    Dynamically discovers and registers all command modules from the 'tools' directory.
    """
    tools_dir = "tools"
    for tool_name in os.listdir(tools_dir):
        tool_path = os.path.join(tools_dir, tool_name)
        if os.path.isdir(tool_path) and 'cli.py' in os.listdir(tool_path):
            try:
                # Dynamically import the 'app' object from the tool's cli.py
                module = importlib.import_module(f'tools.{tool_name}.cli')
                if hasattr(module, 'app'):
                    main_app.add_typer(module.app, name=tool_name)
                    # console.print(f"✅ Registered command: [bold green]{tool_name}[/bold green]")
            except ImportError as e:
                console.print(f"❌ Failed to register command '{tool_name}': {e}", style="bold red")

if __name__ == "__main__":
    register_commands()
    main_app()