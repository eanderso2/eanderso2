import webbrowser
print("Do you want to go to https://github.com/eanderso2/shiny-octo-engine [Y/n]")
if input().lower() == "n" or "no":
  webbrowser.open("https://github.com/eanderso2/shiny-octo-engine")
else:
  print("Okay.")
  exit()
