import sys
import os
import shutil
import subprocess
import platform

if not os.path.exists("build_wasm"):
    os.mkdir("build_wasm")
os.chdir("build_wasm")

if platform.system() == "Windows":
    subprocess.check_call(["cmd", "/c", "emcmake", "cmake",
                           "-G", "MinGW Makefiles", "../src/"])
    subprocess.check_call(["mingw32-make"])
else:
    subprocess.check_call(["command", "emcmake", "cmake", "../src/"])
    subprocess.check_call(["make"])

effekseer_core_js = os.path.join(".", "effekseer.core.js")
effekseer_src_js = os.path.join("..", "src", "js", "effekseer.src.js")
effekseer_js = os.path.join("..", "Release", "effekseer.js")
effekseer_min_js = os.path.join("..", "Release", "effekseer.min.js")

outfile_js = open(effekseer_js, "w")
outfile_min_js = open(effekseer_min_js, "w")

with open(effekseer_core_js) as infile:
    data = infile.read()
    outfile_js.write(data)
    outfile_min_js.write(data)
with open(effekseer_src_js) as infile:
    data = infile.read()
    data_es5 = dukpy.babel_compile(data)["code"]
    outfile_js.write(data_es5)
    outfile_min_js.write(jsmin.jsmin(data_es5))