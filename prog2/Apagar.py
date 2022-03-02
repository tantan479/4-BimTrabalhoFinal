from dao.UsuarioDao import UsuarioDao
from config.Config import Config
from config.Database import Database

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)

