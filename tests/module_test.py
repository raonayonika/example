from example_project.module1 import main

def test_main(capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"


