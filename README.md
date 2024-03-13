# The Language of Large Language Models

https://markmc.github.io/the-language-of-llms/

One of the challenging things aspects of learning about Machine Learning. And some
of the terminology seems unnecessarily obscure - e.g. the act of asking a model
to produce a prediction can be called "forward pass", "inference", etc.

This repo holds a short presentation focused entirely on explaining some of this
terminology in simple terms to newbies who might be finding the terminology
overwhelming.

But why write the presentation myself? Why not have an LLM do it?

Try it out!

```
$ python -m venv venv
$ . ./venv/bin/activate
(venv)> pip install -U pip
(venv)> pip install -U -r requirements.txt
(venv)> make
...
python generate.py > reveal.js-master/index.html
...
(venv)> make open
```
