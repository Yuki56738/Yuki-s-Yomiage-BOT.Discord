def return_token():
  TOKEN=""
  with open("./token.txt", "r") as f:
    TOKEN = f.read()
  return TOKEN
if __name__ == "__main__":
  return_token()