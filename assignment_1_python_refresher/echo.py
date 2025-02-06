def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo"""
    echo_effect = ""  # Echo effect will store the resulting "echo" sound of the input text, modeled by truncating the input text in accordance to the number of repitions, truncating the resulting line by 1 until the number of repetitions is reached.
    if repetitions >= len(
        text
    ):  # If the number of repetitions exceeds the length of the input text, just start at the first letter of text
        for i in range(len(text)):
            echo_effect += text[i:] + "\n"
    else:  # If the number of repetitions is less than the length of the input text, start at the len(text) - repetitions index of the input text and proceed to the end.
        for i in range(len(text) - repetitions, len(text)):
            echo_effect += text[i:] + "\n"

    echo_effect += ".\n"  # Add a blank line with just a period to end the echo effect.
    return echo_effect


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
