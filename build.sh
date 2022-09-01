function build() {
  poetry run nuitka --onefile "src/$1.py"

  rm -rf "$1.build/"
	rm -rf "$1.dist/"
	rm -rf "$1.onefile-build/"

	mkdir "./bin"
	mv "$1.bin" "./bin/$1"
}

build main
