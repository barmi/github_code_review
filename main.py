import sys

from PyQt5.QtWidgets import QApplication

from tobeui.TWindowManager import TWindowManager

from avn_simulator.TIntroWindow import TIntroWindow
from avn_simulator.TMainWindow import TMainWindow
from avn_simulator.TMapWindow import TMapWindow
from avn_simulator.TSettingWindow import TSettingWindow
from avn_simulator.TVehicleCheckSuccessWindow import TVehicleCheckSuccessWindow
from avn_simulator.TVehicleCheckFailedWindow import TVehicleCheckFailedWindow
from avn_simulator.TSetAmountWindow import TSetAmountWindow
from avn_simulator.TPaymentApprovalWindow import TPaymentApprovalWindow
from avn_simulator.TPaymentDeclinedWindow import TPaymentDeclinedWindow
from avn_simulator.TServiceUsedWindow import TServiceUsedWindow
from avn_simulator.TServiceCompletedWindow import TServiceCompletedWindow
from avn_simulator.TPathWindow import TPathWindow

from network.PacketServer import ThreadTcpServer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wm = TWindowManager().instance()

    wm.addWindow(TIntroWindow("intro_window"))
    wm.addWindow(TMainWindow("main_window"))
    wm.addWindow(TSettingWindow("setting_window"))
    wm.addWindow(TMapWindow("map_window"))

    wm.addWindow(TVehicleCheckSuccessWindow("vehiclecheck_success_window"))
    wm.addWindow(TVehicleCheckFailedWindow("vehiclecheck_failed_window"))
    wm.addWindow(TSetAmountWindow("set_amount_window"))
    wm.addWindow(TPaymentApprovalWindow("payment_approval_window"))
    wm.addWindow(TPaymentDeclinedWindow("payment_declined_window"))
    wm.addWindow(TServiceUsedWindow("service_used_window"))
    wm.addWindow(TServiceCompletedWindow("service_completed_window"))
    wm.addWindow(TPathWindow("path_window"))

    intro_window = wm.findWindow("intro_window")
    intro_window.showWindow()

    ThreadTcpServer().start()

    sys.exit(app.exec_())
