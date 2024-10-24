from AnonXMusic.core.bot import Anony
from AnonXMusic.core.dir import dirr
from AnonXMusic.core.git import git
from AnonXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()

