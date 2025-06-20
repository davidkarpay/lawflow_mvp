import json
import subprocess
import typer
from pathlib import Path

app = typer.Typer(help="Lawflow CLI")

@app.command("test")
def test_all(
    modules: list[str] = typer.Option(
        None, "--all", help="Run tests for all services"
    )
):
    """
    Run pytest in every service folder and emit a JSON summary.
    """
    services_dir = Path(__file__).parent.parent / "services"
    results = {}

    # Determine targets: all services or a subset
    targets = services_dir.iterdir() if modules is None else [
        services_dir / m for m in modules
    ]

    for service in targets:
        if not service.is_dir():
            continue
        test_path = service / "tests"
        test_cmd = [
            "pytest",
            str(test_path),
            "--maxfail=1",
            "--disable-warnings",
            "--quiet",
        ]
        proc = subprocess.run(test_cmd, capture_output=True, text=True)
        results[service.name] = {
            "return_code": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }

    typer.echo(json.dumps({"results": results}, indent=2))
    # Exit code reflects overall test success
    raise typer.Exit(code=0 if all(r["return_code"] == 0 for r in results.values()) else 1)

if __name__ == "__main__":
    app()
