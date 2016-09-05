This is an Alfred 3 workflow to search Genius for lyrics. By default it will 
search for the currently playing track.

This workflow is *not* particularly easy for end-users to install. 
You will need to install Python 3 and register with Genius for an API token.
If you think Python is a type of snake this might not be for you.

## Installation:

### Prep:

You'll need a Python 3 install with the `requests` package. 

I used [conda][conda install] for this:

    conda create -n alfred-genius python=3.5 requests

But feel free to use python3 from Homebrew or something else.

### Configuration

- Set the `PATH` var for this workflow to your Python bin
- Set the `GENIUS_TOKEN` var to your Genius [API token][genius api]

***

Useful development links:

- https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
- https://www.alfredapp.com/help/workflows/utilities/debug/
- https://github.com/dtinth/JXA-Cookbook/wiki/Getting-the-Application-Instance

[conda install]: http://conda.pydata.org/docs/install/quick.html#os-x-miniconda-install
[genius api]: https://genius.com/api-clients
