# Getting started with Project 1

Install [q][1] in order to run SQL directly on TSV files:

```shell-session
$ sudo apt update
$ sudo apt install python3-q-text-as-data
```

Clone the GitHub repository:

```shell-session
$ git clone https://github.com/ProfAvery/cpsc349-project1.git
```

Download the [Unsplash Lite dataset][2] and extract some pet photos:

``` shell-session
$ cd cpsc349-project/unsplash
$ make
```

Install and start the [Eleventy static site generator][3]:

```shell-session
$ cd ..
$ npm install
$ npm start

```

Open the [newly generated site][4].

[1]: https://harelba.github.io/q/
[2]: https://github.com/unsplash/datasets
[3]: https://www.11ty.dev/
[4]: http://localhost:8080/
