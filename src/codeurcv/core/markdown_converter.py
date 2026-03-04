class MarkdownConverter:
    @staticmethod
    def convert(text: str) -> str:
        import subprocess

        result = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "latex"],
            input=text,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()