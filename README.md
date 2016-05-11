# Twitter Search

This is simple, python based twitter search script that uses tweepy package to search for public tweets.

In order to make this script work, you need to supply twitter keys to `config.py` file. There you can see what and how to get required keys.

There is `run.py` file which can be used directly after updating `config.py` file. This will retrieve tweets from provided data.

see `$ python run.py -h`  for more info.


Setup
---
I recommend using virtual environment to isolate your project.
Following are the steps to setup and run the scripts after updating `config.py` file.

```
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python run.py -k football -l 5
```

This will search 5 public tweets with text ***football*** in it.
