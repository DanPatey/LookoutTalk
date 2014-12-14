LookoutTalk
===========

Slides and Examples from my SauceLabs talk at LookoutHQ on 12/11/2014


#Pip / VirtualEnv / DDT Fresh Install:

##Install
sudo easy_install pip

sudo pip install virtualenv



##Create Environment

virtualenv env

ls env

env/bin/python

which python (returns global python binary)



##Alias The Environment

source env/bin/activate

which python (returns virtualenv python binary)

which pip

sudo pip install -r requirements.txt

##List of Example Files

<ul>
<li>0generatortest.py -- An example of how a generator iterates through yield producing results but does not store anything in memory.
<li>0oldway.py -- An example of the old way of asserting a test one-by-one.
<li>0newway.py -- An example of the same test but asserting it with multiple variables.
<li>1decoratortest.py -- An example to show that you can run the test with a * or without in order to create a generator that will multiply our test cases.
<li>2logintest.py -- data/users.py -- An example showing how we can keep our data in a seperate file and create a function that we can re-use with every test.
<li>3big_example.py -- data/sample_data.py -- pages/page_class.py(Note this should be a CSS map, I'll be changing this soon --- A close to real-world example of how we can use a test to call to a class that stores information to manipulate our data. We split our tests into multiple suites and provide any information we need to input in the data file as well.
</ul>

##Thanks To

<ul>
<li>https://technomilk.wordpress.com TechnoMilk for creating DDT and proving examples on his blog
<li>http://ddt.readthedocs.org/ for an explanation of nosetests
<li>http://swordstyle.com/func_test_tutorial/part_one/extra_generative_tests.html for a fantastic example and explanation of generators
