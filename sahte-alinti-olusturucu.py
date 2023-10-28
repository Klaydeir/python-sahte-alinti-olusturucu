import random

# source: http://en.wikipedia.org/wiki/Python_%28programming_language%29
sentences = "Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale. Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library. Python interpreters are available for installation on many operating systems, allowing Python code execution on a wide variety of systems. Using third-party tools, such as Py2exe or Pyinstaller,[24] Python code can be packaged into stand-alone executable programs for some of the most popular operating systems, allowing for the distribution of Python-based software for use on those environments without requiring the installation of a Python interpreter. CPython, the reference implementation of Python, is free and open-source software and has a community-based development model, as do nearly all of its alternative implementations. CPython is managed by the non-profit Python Software Foundation.".split(".")

print(("-" * 30) + "\nSözde Alıntı Oluşturucu\n" + ("-" * 30))

n = int(input("Kaç Tane Cümle Oluşturulsun ?: "))

quote = []

for i in range(n):
    quote.append(random.choice(sentences))

print("Your pseudo quote: {}.".format(".".join(quote)))