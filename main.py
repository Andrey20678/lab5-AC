
from database.database import *
from database.models import *
from sqlalchemy.orm import Session
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(873, 500)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 201, 211))
        self.groupBox.setObjectName("groupBox")
        self.tAdd = QtWidgets.QPushButton(self.groupBox)
        self.tAdd.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.tAdd.setObjectName("tAdd")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_3.setObjectName("label_3")
        self.tTypeBox = QtWidgets.QComboBox(self.groupBox)
        self.tTypeBox.setGeometry(QtCore.QRect(10, 90, 181, 22))
        self.tTypeBox.setObjectName("tTypeBox")
        self.tDelBox = QtWidgets.QComboBox(self.groupBox)
        self.tDelBox.setGeometry(QtCore.QRect(10, 150, 181, 22))
        self.tDelBox.setObjectName("tDelBox")
        self.tDel = QtWidgets.QPushButton(self.groupBox)
        self.tDel.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.tDel.setObjectName("tDel")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(10, 40, 181, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 10, 221, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.typeAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.typeAdd.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.typeAdd.setObjectName("typeAdd")
        self.typeName = QtWidgets.QLineEdit(self.groupBox_2)
        self.typeName.setGeometry(QtCore.QRect(10, 40, 201, 20))
        self.typeName.setObjectName("typeName")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_11.setObjectName("label_11")
        self.typeSpeed = QtWidgets.QLineEdit(self.groupBox_2)
        self.typeSpeed.setGeometry(QtCore.QRect(10, 90, 201, 20))
        self.typeSpeed.setObjectName("typeSpeed")
        self.typeDel = QtWidgets.QPushButton(self.groupBox_2)
        self.typeDel.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.typeDel.setObjectName("typeDel")
        self.typeDelBox = QtWidgets.QComboBox(self.groupBox_2)
        self.typeDelBox.setGeometry(QtCore.QRect(10, 150, 201, 22))
        self.typeDelBox.setObjectName("typeDelBox")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 201, 260))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cityAdd = QtWidgets.QPushButton(self.groupBox_3)
        self.cityAdd.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.cityAdd.setObjectName("cityAdd")
        self.cityName = QtWidgets.QLineEdit(self.groupBox_3)
        self.cityName.setGeometry(QtCore.QRect(10, 40, 181, 20))
        self.cityName.setObjectName("cityName")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_14.setObjectName("label_14")
        self.cityDel = QtWidgets.QPushButton(self.groupBox_3)
        self.cityDel.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.cityDel.setObjectName("cityDel")
        self.cityDelBox = QtWidgets.QComboBox(self.groupBox_3)
        self.cityDelBox.setGeometry(QtCore.QRect(10, 200, 181, 22))
        self.cityDelBox.setObjectName("cityDelBox")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(220, 230, 221, 260))
        self.groupBox_4.setObjectName("groupBox_4")
        self.statAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.statAdd.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.statAdd.setObjectName("statAdd")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_16.setObjectName("label_16")
        self.statName = QtWidgets.QLineEdit(self.groupBox_4)
        self.statName.setGeometry(QtCore.QRect(10, 90, 201, 20))
        self.statName.setObjectName("statName")
        self.statCity = QtWidgets.QComboBox(self.groupBox_4)
        self.statCity.setGeometry(QtCore.QRect(10, 40, 201, 22))
        self.statCity.setObjectName("statCity")
        self.statDel = QtWidgets.QPushButton(self.groupBox_4)
        self.statDel.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.statDel.setObjectName("statDel")
        self.statDelBox = QtWidgets.QComboBox(self.groupBox_4)
        self.statDelBox.setGeometry(QtCore.QRect(10, 200, 201, 22))
        self.statDelBox.setObjectName("statDelBox")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(450, 10, 201, 211))
        self.groupBox_5.setObjectName("groupBox_5")
        self.routeAdd = QtWidgets.QPushButton(self.groupBox_5)
        self.routeAdd.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.routeAdd.setObjectName("routeAdd")
        self.routeName = QtWidgets.QLineEdit(self.groupBox_5)
        self.routeName.setGeometry(QtCore.QRect(10, 40, 181, 20))
        self.routeName.setObjectName("routeName")
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_20.setObjectName("label_20")
        self.routeDel = QtWidgets.QPushButton(self.groupBox_5)
        self.routeDel.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.routeDel.setObjectName("routeDel")
        self.routeDelBox = QtWidgets.QComboBox(self.groupBox_5)
        self.routeDelBox.setGeometry(QtCore.QRect(10, 150, 181, 22))
        self.routeDelBox.setObjectName("routeDelBox")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(450, 230, 201, 260))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pointAdd = QtWidgets.QPushButton(self.groupBox_6)
        self.pointAdd.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.pointAdd.setObjectName("pointAdd")
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(10, 120, 161, 16))
        self.label_25.setObjectName("label_25")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_6)
        self.timeEdit.setGeometry(QtCore.QRect(10, 140, 181, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.statBox = QtWidgets.QComboBox(self.groupBox_6)
        self.statBox.setGeometry(QtCore.QRect(10, 90, 181, 22))
        self.statBox.setObjectName("statBox")
        self.routeBox = QtWidgets.QComboBox(self.groupBox_6)
        self.routeBox.setGeometry(QtCore.QRect(10, 40, 181, 22))
        self.routeBox.setObjectName("routeBox")
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_26.setObjectName("label_26")
        self.pointDel = QtWidgets.QPushButton(self.groupBox_6)
        self.pointDel.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.pointDel.setObjectName("pointDel")
        self.pointDelBox = QtWidgets.QComboBox(self.groupBox_6)
        self.pointDelBox.setGeometry(QtCore.QRect(10, 200, 181, 22))
        self.pointDelBox.setObjectName("pointDelBox")
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(660, 10, 201, 211))
        self.groupBox_7.setObjectName("groupBox_7")
        self.tRouteChange = QtWidgets.QPushButton(self.groupBox_7)
        self.tRouteChange.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.tRouteChange.setObjectName("tRouteChange")
        self.tRouteDel = QtWidgets.QPushButton(self.groupBox_7)
        self.tRouteDel.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.tRouteDel.setObjectName("tRouteDel")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_5.setObjectName("label_5")
        self.tRouteBox = QtWidgets.QComboBox(self.groupBox_7)
        self.tRouteBox.setGeometry(QtCore.QRect(10, 90, 181, 22))
        self.tRouteBox.setObjectName("tRouteBox")
        self.tBox = QtWidgets.QComboBox(self.groupBox_7)
        self.tBox.setGeometry(QtCore.QRect(10, 40, 181, 22))
        self.tBox.setObjectName("tBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "БД общественного транспорта"))
        self.groupBox.setTitle(_translate("Dialog", "Добавить транспортное средство"))
        self.tAdd.setText(_translate("Dialog", "Добавить"))
        self.label_2.setText(_translate("Dialog", "Дата ввода в эсксплуатацию"))
        self.label_3.setText(_translate("Dialog", "Тип транспорного средства"))
        self.tDel.setText(_translate("Dialog", "Удалить"))
        self.groupBox_2.setTitle(_translate("Dialog", "Добавить тип транспортного средства"))
        self.typeAdd.setText(_translate("Dialog", "Добавить"))
        self.label_10.setText(_translate("Dialog", "Название"))
        self.label_11.setText(_translate("Dialog", "Средняя возможная скорость"))
        self.typeDel.setText(_translate("Dialog", "Удалить"))
        self.groupBox_3.setTitle(_translate("Dialog", "Добавить город"))
        self.cityAdd.setText(_translate("Dialog", "Добавить"))
        self.label_14.setText(_translate("Dialog", "Название"))
        self.cityDel.setText(_translate("Dialog", "Удалить"))
        self.groupBox_4.setTitle(_translate("Dialog", "Добавить остановку"))
        self.statAdd.setText(_translate("Dialog", "Добавить"))
        self.label_15.setText(_translate("Dialog", "Город"))
        self.label_16.setText(_translate("Dialog", "Название"))
        self.statDel.setText(_translate("Dialog", "Удалить"))
        self.groupBox_5.setTitle(_translate("Dialog", "Добавить маршрут"))
        self.routeAdd.setText(_translate("Dialog", "Добавить"))
        self.label_20.setText(_translate("Dialog", "Название"))
        self.routeDel.setText(_translate("Dialog", "Удалить"))
        self.groupBox_6.setTitle(_translate("Dialog", "Добавить точку в  маршрут"))
        self.pointAdd.setText(_translate("Dialog", "Добавить"))
        self.label_24.setText(_translate("Dialog", "Остановка"))
        self.label_25.setText(_translate("Dialog", "Время"))
        self.label_26.setText(_translate("Dialog", "Маршрут"))
        self.pointDel.setText(_translate("Dialog", "Удалить"))
        self.groupBox_7.setTitle(_translate("Dialog", "Присвоить маршрут"))
        self.tRouteChange.setText(_translate("Dialog", "Изменить"))
        self.tRouteDel.setText(_translate("Dialog", "Убрать"))
        self.label_5.setText(_translate("Dialog", "Маршрут"))
        self.label_6.setText(_translate("Dialog", "Транспортное средство"))

    def setupEL(self):
        def ad(a,f): a.clicked.connect(f)

        ad(self.cityAdd, self.Add_city)
        ad(self.cityDel, self.Del_city)
        ad(self.statAdd, self.Add_stat)
        ad(self.statDel, self.Del_stat)
        ad(self.routeAdd, self.Add_route)
        ad(self.routeDel, self.Del_route)
        ad(self.pointAdd, self.Add_point)
        ad(self.pointDel, self.Del_point)
        ad(self.typeAdd, self.Add_type)
        ad(self.typeDel, self.Del_type)
        ad(self.tAdd, self.Add_transport)
        ad(self.tDel, self.Del_transport)
        ad(self.tRouteChange, self.Change_route)
        ad(self.tRouteDel, self.Del_change_route)

        self.updateAll()

    def updateAll(self):
        self.updateCities()
        self.updateStations()
        self.updateRoutes()
        self.updatePoints()
        self.updateTypes()
        self.updateTransport()

    def updateCities(self):
        cities = get_selection(Cities.city_Name)
        self.cityDelBox.clear()
        self.cityDelBox.addItems(cities)
        self.statCity.clear()
        self.statCity.addItems(cities)

    def updateStations(self):
        stats = get_selection(Stations.station_Name)
        self.statDelBox.clear()
        self.statDelBox.addItems(stats)
        self.statBox.clear()
        self.statBox.addItems(stats)

    def updateRoutes(self):
        routes = get_selection(Routes.route_Name)
        self.routeDelBox.clear()
        self.routeDelBox.addItems(routes)
        self.routeBox.clear()
        self.routeBox.addItems(routes)
        self.tRouteBox.clear()
        self.tRouteBox.addItems(routes)

    def updatePoints(self):
        points = get_selection2(RoutesStructure)
        self.pointDelBox.clear()
        for point in points:
            n = point.route.route_Name
            s = point.station.station_Name
            t = f"{point.time.time()}"[0:5]
            self.pointDelBox.addItem(f"{n} {s} {t}")
    
    def updateTypes(self):
        types = get_selection2(TransportTypes)
        self.typeDelBox.clear()
        self.tTypeBox.clear()
        for typ in types:
            n = typ.type_Name
            s = typ.type_Average_Speed
            self.typeDelBox.addItem(f"{n} {s}")
            self.tTypeBox.addItem(f"{n} {s}")

    def updateTransport(self):
        ts = get_selection2(Transport)
        self.tDelBox.clear()
        self.tBox.clear()
        for t in ts:
            i = t.ts_ID
            tt = t.type.type_Name
            cd = t.commissioning_date.date()
            if (t.route):
                r = t.route.route_Name
            else:
                r = ""
            self.tDelBox.addItem(f"{i} {tt} {cd} {r}")
            self.tBox.addItem(f"{i} {tt} {cd} {r}")


    def Add_city(self):
        text = self.cityName.text()
        if (text.__len__()<3): return
        add_city(text)
        self.updateCities()

    def Add_stat(self):
        text = self.statName.text()
        ind = self.statCity.currentIndex()
        if (text.__len__()<3 or ind is None): return
        add_stat(text, ind)
        self.updateStations()

    def Add_route(self):
        text = self.routeName.text()
        if (text.__len__()<3): return
        add_route(text)
        self.updateRoutes()

    def Add_point(self):
        route = self.routeBox.currentIndex()
        stat = self.statBox.currentIndex()
        time = self.timeEdit.dateTime().toPyDateTime()
        if (route is None or stat is None): return
        add_point(route,stat,time)
        self.updatePoints()

    def Add_type(self):
        try:
            text1 = self.typeName.text()
            text2 = int(self.typeSpeed.text())
            if (text1.__len__()<3 or text2<5): return
        except:
            return
        finally:
            add_type(text1, text2)
            self.updateTypes()

    def Add_transport(self):
        date = self.dateEdit.dateTime().toPyDateTime()
        typ = self.tTypeBox.currentIndex()
        if (typ is None): return
        add_transport(date, typ)
        self.updateTransport()

    def Change_route(self):
        ts = self.tBox.currentIndex()
        route = self.tRouteBox.currentIndex()
        if (ts is None or route is None): return
        change_transport_route(ts, route)
        self.updateTransport()

    def Del_change_route(self):
        ts = self.tBox.currentIndex()
        if (ts is None): return
        change_transport_route(ts)
        self.updateTransport()


    def Del_city(self):
        ind = self.pointDelBox.currentIndex()
        if (ind is None): return
        del_by_id(ind, Cities)
        self.updateAll()

    def Del_stat(self):
        ind = self.pointDelBox.currentIndex()
        if (ind is None): return
        del_by_id(ind, Stations)
        self.updateAll()
    
    def Del_route(self):
        ind = self.pointDelBox.currentIndex()
        if (ind is None): return
        del_by_id(ind, Routes)
        self.updateAll()

    def Del_point(self):
        ind = self.pointDelBox.currentIndex()
        if (ind is None): return
        del_by_id(ind, RoutesStructure)
        self.updateAll()

    def Del_type(self):
        ind = self.typeDelBox.currentIndex()
        if (ind is None): return
        del_by_id(ind, TransportTypes)
        self.updateAll()

    def Del_transport(self):
        ind = self.tDelBox.currentIndex()
        if (ind is None): return
        del_by_id(ind, Transport)
        self.updateAll()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.setupEL()
    Dialog.show()
    sys.exit(app.exec_())

