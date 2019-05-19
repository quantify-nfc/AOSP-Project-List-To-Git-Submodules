projectList = open("project.list", "r")
gitSubmodulesFile = open(".gitsubmodules", "w+")

submodules = []

for project in projectList:
    p = project.rstrip()
    submoduleText = ""
    submoduleText += "[submodule \"" + p + "\"]" + "\n"
    submoduleText += "        path = " + p + "\n"
    submoduleText += "        url = https://android.googlesource.com/platform/" + p + "\n"

    submodules.append(submoduleText)

out = ""

for submodule in submodules:
    out += submodule

gitSubmodulesFile.write(out)

projectList.close()
gitSubmodulesFile.close()
