
""" To document """

from pygame_screenflow import ScreenFlow

def get_wifi_networks():
    """ returns wifi network. """
    return None

class Application(ScreenFlow):
    """ Simple wifi connect application """
    def __init__(self):
        """ Default constructor. """
        ScreenFlow.__init__(self)
        self.load_from_file('screenflow.xml')
        # Configure first screen.
        self.wifi_prompt.no.on_select(self.quit)
        self.wifi_prompt.yes.on_select(self.navigate_to(self.wifi_select))
        # Configure second screen.
        self.wifi_select.provider = get_wifi_networks
        self.wifi_select.renderer = None # TODO Set custom renderer.
        self.wifi_select.listener = None # TODO : Switch to view.
        self.wifi_select.on_select(self.navigate_to(self.wifi_passphrase))
        self.wifi_passphrase.on_validate(None)

if __name__ == '__main__':
    application = Application()
    application.run()
