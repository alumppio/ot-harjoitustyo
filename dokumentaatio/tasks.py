from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True) #When the game is ready

@task
def test(ctx):
    ctx.run("pytest src", pty=True)


#Copied straight from the Todo-app's sourcecode
@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src', pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)