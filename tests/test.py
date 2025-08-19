from src.run import run


def test_run_without_cwd():
    assert run() == 0

def test_run_with_cwd(cwd_to_src):
    assert run() == 0

def test_cwd_without_run(cwd_to_src):
    assert run(dry_run=True) == 42

def test_run_not_python_with_cwd(cwd_to_src):
    assert run(["more"]) == 0
