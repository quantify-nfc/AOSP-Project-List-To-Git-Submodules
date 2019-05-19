projectList = open("project.list", "r")
gitSubmodulesFile = open(".gitsubmodules", "w+")

submodules = []

for project in projectList:
    submoduleText = ""
    submoduleText += "[submodule \"" + project + "\"]" + "\n"
    submoduleText += "        path = " + project + "\n"
    submoduleText += "        url = https://android.googlesource.com/platform/" + project + "\n"

    submodules.append(submoduleText)

out = ""

for submodule in submodules:
    out += submodule

gitSubmodulesFile.write(out)

projectList.close()
gitSubmodulesFile.close()
