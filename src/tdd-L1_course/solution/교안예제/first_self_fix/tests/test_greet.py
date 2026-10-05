from greet import print_greeting


def test_greeting_is_checked(capsys):  # ✅ 출력을 붙잡아 assert
    print_greeting("World")
    assert capsys.readouterr().out == "Hello, World!\n"
