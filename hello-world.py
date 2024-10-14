import os

def main():
  name = os.getenv("USERNAME")
  print(f"¡Hello {name} from GitHub!")

if __name__ == "__main__":
  main()
