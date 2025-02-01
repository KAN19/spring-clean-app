import click

from spring_clean_app.actions import download_project
from spring_clean_app.actions.project_structure import create_boilerplate


@click.group()
def cli():
    """Main entry point for the CLI."""
    pass


@click.command()
def create():
    # 1. Get Basic configuration for download project
    build_tool_map = {"gradle": "gradle-project", "maven": "maven-project"}
    while True:
        build_tool = build_tool_map.get(
            click.prompt("Enter build tool", default="maven")
        )
        if build_tool != None:
            break
        else:
            click.echo("Error!! The value should be either maven or gradle")

    group_id = click.prompt("Enter groupId", default="com.example")
    artifact_id = click.prompt("Enter artifactId", default="demo")

    # 2. Select more option
    # lombok,web,flyway,mysql,validation,data-jpa
    dependencies = ["lombok,web,flyway,validation,data-jpa,webflux"]
    database = click.prompt("Enter database type. Supporting [mysql]", default="mysql")
    dependencies.append(database)

    # 3. download project
    options = {
        "type": build_tool,
        "language": "java",
        "packaing": "jar",
        "groupId": group_id,
        "artifactId": artifact_id,
        "name": artifact_id,
        "dependencies": ",".join(dependencies),
        "database": database,
    }
    path = download_project.download(options)
    # 3. Adjust project with clean architecture
    create_boilerplate(path, options)


cli.add_command(create, name="init")

if __name__ == "__main__":
    cli()
