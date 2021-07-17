# Getting started with Project 1

Install [q][1] in order to run SQL directly on TSV files:

```shell-session
$ sudo apt update
$ sudo apt install python3-q-text-as-data
```

[Fork][2] the GitHub [cpsc349-project1][3] repository, then [clone][4]
your forked repository locally:

```shell-session
$ git clone https://github.com/USERNAME/cpsc349-project1.git
```


Download the [Unsplash Lite dataset][5] and extract some pet photos:

``` shell-session
$ cd cpsc349-project1/unsplash
$ make
```

Install and start the [Eleventy static site generator][6]:

```shell-session
$ cd ..
$ npm install
$ npm start

```

Open the [newly generated site][7].


[1]: https://harelba.github.io/q/
[2]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[3]: https://github.com/ProfAvery/cpsc349-project1
[4]: https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository
[5]: https://github.com/unsplash/datasets
[6]: https://www.11ty.dev/
[7]: http://localhost:8080/
