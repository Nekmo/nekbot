NekBot
######

Quick Start
===========

My first app
------------
Use the ``createapp`` command to create your new awesome app. Let's call it *"hello"*, for example::

    $ ./bot.py createapp hello

A new folder called *"hello"* will be created. Inside, there will be a handlers.py file. Here you can
register the watchers. This is an example:


.. code-block:: python

    from nekbot.handler import CommandHandler, HandlerRegister
    from hello.app import HelloApp
    from nekbot.message.text import TextMessage

    register = HandlerRegister(HelloApp)


    @register(CommandHandler('hello'))
    def hello(bot, message):
        message.chat.send_message('Hello world!')


You can also use classes:

.. code-block:: python

    ...

    @register(CommandHandler('hello'))
    class Hello(TextMessage):
        def get_body(self):
            return "Hello world!"

Or shorter, and with support for emoji and arguments:

.. code-block:: python

    ...

    @register(CommandHandler('hello'))
    class Hello(TextMessage):
        body = "Hello {message.user.name}! :thumbsup:"
