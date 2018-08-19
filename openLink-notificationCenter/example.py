import re
import BigWorld
from gui.SystemMessages import SM_TYPE
from gui.SystemMessages import pushMessage
from notification.settings import NOTIFICATION_TYPE
from gui.Scaleform.daapi.view.lobby.LobbyView import LobbyView
from notification.actions_handlers import NotificationsActionsHandlers

def new_handleAction(self, model, typeID, entityID, actionName):
    if typeID == NOTIFICATION_TYPE.MESSAGE and re.match('https?://', actionName, re.I):
        BigWorld.wg_openWebBrowser(actionName)
    else:
        old_handleAction(self, model, typeID, entityID, actionName)


old_handleAction = NotificationsActionsHandlers.handleAction
NotificationsActionsHandlers.handleAction = new_handleAction

def NewLobbyView_populate(self):
    OldLobbyView_populate(self)
    global Show
    if not Show:
        Show = True
        pushMessage(u'<a href="event:https://ekspoint-mods.ru/"><font color="#eb2222">ekspoint-mods.ru</font></a>', SM_TYPE.GameGreeting)


Show = False
OldLobbyView_populate = LobbyView._populate
LobbyView._populate = NewLobbyView_populate
