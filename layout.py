from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from tkinter import *
from tkinter import font as tkFont
import tkinter.messagebox as tkm
from sofifa import sofifa
from pes6es import pes6es

class app_layout:
    def __init__(self):
        self.__appname = 'SoFIFA Scraper'
        self.__pad = 5
        self.__win = Tk()
        self.__win.title(self.__appname)
        self.__win.iconbitmap('logo.ico')
        self.__win.resizable(False, False)
        self.player_list = []
        self.column_sort = 0
        self.pes6es = pes6es()
        self.sofifa = sofifa()
        self.__font = tkFont.Font(family='Consolas', size=10, weight='normal')
        self.__bgcolor = '#6633FF'
        self.__fgcolor = '#FFFFFF'
        self.__style = Style()
        self.__player_stats = ''
    
    def __window_close(self):
        if tkm.askokcancel(self.__appname, 'Do you want to quit?'):
            self.__win.destroy()

    def __about_app(self):
        msg = 'Edgar Santa Rosa (C) 2022\nGitHub: https://github.com/EdgarOSR'
        tkm.showinfo(self.__appname, msg)

    ### APP LAYOUT: BUTTONS, LABELS, ENTRIES ###
    def __app_labels(self):
        self.lbGame = Label(self.__win)
        self.lbVersion = Label(self.__win)
        self.lbCountry = Label(self.__win)
        self.lbClub = Label(self.__win)
        self.lbMinOvr = Label(self.__win)
        self.lbMaxOvr = Label(self.__win)
        self.lbSearch = Label(self.__win)
        self.lbPlayerID = Label(self.__win)
        self.lbPlayerName = Label(self.__win)
        
    def __app_entries(self):
        self.txGame = Combobox(self.__win)
        self.txVersion = Combobox(self.__win)
        self.txCountry = Combobox(self.__win)
        self.txClub = Combobox(self.__win)
        self.txMinOvr = Combobox(self.__win)
        self.txMaxOvr = Combobox(self.__win)
        self.txSearch = Combobox(self.__win)
        self.txPlayerID = Entry(self.__win)
        self.txPlayerName = Entry(self.__win)
        self.txGameHidden = Combobox(self.__win)
        self.txVersionHidden = Combobox(self.__win)
        self.txCountryHidden = Combobox(self.__win)
        self.txClubHidden = Combobox(self.__win)
        self.txPlayerList = Treeview(self.__win)
    
    def __app_buttons(self):
        self.btConvert = Button(self.__win)
        self.btClipboard = Button(self.__win)
        self.btAbout = Button(self.__win)
        self.btConvertClassic = Button(self.__win)

    def __app_config(self):
        self.__win.option_add('*TCombobox*Listbox.font', self.__font)
        self.__style.configure('Treeview', font=self.__font)
        self.lbGame.config(text='Game', width=10, justify='left', font=self.__font, anchor='w')
        self.lbVersion.config(text='Version', width=10, justify='left', font=self.__font, anchor='w')
        self.lbCountry.config(text='Country', width=10, justify='left', font=self.__font, anchor='w')
        self.lbClub.config(text='Club', width=10, justify='left', font=self.__font, anchor='w')
        self.lbMinOvr.config(text='MinOVR', width=10, justify='left', font=self.__font, anchor='w')
        self.lbMaxOvr.config(text='MaxOVR', width=10, justify='left', font=self.__font, anchor='w')
        self.lbSearch.config(text='SearchType', width=10, justify='left', font=self.__font, anchor='w')
        self.lbPlayerID.config(text='PlayerID', width=10, justify='left', font=self.__font, anchor='w')
        self.lbPlayerName.config(text='PlayerName', width=10, justify='left', font=self.__font, anchor='w')
        self.btConvertClassic.config(text='Old Stats', width=20, bg=self.__bgcolor, fg=self.__fgcolor, font=self.__font)
        self.btConvert.config(text='Convert', width=20, bg=self.__bgcolor, fg=self.__fgcolor, font=self.__font)
        self.btClipboard.config(text='Clipboard', width=20, bg=self.__bgcolor, fg=self.__fgcolor, font=self.__font)
        self.btAbout.config(text='About', width=10, bg=self.__bgcolor, fg=self.__fgcolor, font=self.__font)
        self.txGame.config(width=20, state='readonly', values='', font=self.__font)
        self.txVersion.config(width=20, state='readonly', values='', font=self.__font)
        self.txCountry.config(width=20, state='readonly', values='', font=self.__font)
        self.txClub.config(width=20, state='readonly', values='', font=self.__font)
        self.txMinOvr.config(width=20, state='readonly', values='', font=self.__font)
        self.txMaxOvr.config(width=20, state='readonly', values='', font=self.__font)
        self.txSearch.config(width=20, state='readonly', values='', font=self.__font)
        self.txPlayerID.config(width=20, state='normal', font=self.__font)
        self.txPlayerName.config(width=20, state='normal', font=self.__font)
        self.txGameHidden.config(width=20, state='readonly', values='', font=self.__font)
        self.txVersionHidden.config(width=20, state='readonly', values='', font=self.__font)
        self.txCountryHidden.config(width=20, state='readonly', values='', font=self.__font)
        self.txClubHidden.config(width=20, state='readonly', values='', font=self.__font)
        self.txPlayerList.config(show='headings', selectmode='browse', columns=('bov','name','nation','pos','club'), height=20)
        self.txPlayerList.heading('bov', text='▲ OVR')
        self.txPlayerList.heading('name', text='NAME')
        self.txPlayerList.heading('club', text='CLUB')
        self.txPlayerList.heading('pos', text='POS')
        self.txPlayerList.heading('nation', text='NATION')
        self.txPlayerList.column('bov', width=48)
        self.txPlayerList.column('name', width=150)
        self.txPlayerList.column('nation', width=120)
        self.txPlayerList.column('pos', width=48)
        self.txPlayerList.column('club', width=180)

    def __reset_tree_columns(self):
        self.txPlayerList.heading('bov', text='OVR')
        self.txPlayerList.heading('name', text='NAME')
        self.txPlayerList.heading('nation', text='NATION')
        self.txPlayerList.heading('pos', text='POS')
        self.txPlayerList.heading('club', text='CLUB')

    def __app_grid_config(self):
        self.lbGame.grid(column=0, row=1, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbVersion.grid(column=0, row=2, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbCountry.grid(column=0, row=3, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbClub.grid(column=0, row=4, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbMinOvr.grid(column=0, row=5, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbMaxOvr.grid(column=0, row=6, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbSearch.grid(column=0, row=7, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbPlayerName.grid(column=0, row=8, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.lbPlayerID.grid(column=0, row=9, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.btAbout.grid(column=0, row=10, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.btClipboard.grid(column=0, row=11, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.btConvertClassic.grid(column=0, row=12, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.btConvert.grid(column=0, row=13, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew')
        self.txGame.grid(column=1, row=1, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txVersion.grid(column=1, row=2, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txCountry.grid(column=1, row=3, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txClub.grid(column=1, row=4, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')        
        self.txMinOvr.grid(column=1, row=5, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txMaxOvr.grid(column=1, row=6, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txSearch.grid(column=1, row=7, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txPlayerName.grid(column=1, row=8, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txPlayerID.grid(column=1, row=9, padx=self.__pad, pady=self.__pad, columnspan=1, sticky='nsew')
        self.txPlayerList.grid(column=2, row=0, padx=self.__pad, pady=self.__pad, columnspan=2, sticky='nsew', rowspan=14)

    ### SCRAP COMBO BOXES VALUES ###
    def load_combo_game(self):
        self.txGame['values'], self.txGameHidden['values'] = self.sofifa.get_games()
        self.txGame.current(0)
        self.txGameHidden.current(0)
    
    def load_combo_version(self):
        game = str(self.txGameHidden.get())
        self.txVersion['values'], self.txVersionHidden['values'] = self.sofifa.get_versions(game)
        self.txVersion.current(0)
        self.txVersionHidden.current(0)

    def load_combo_country(self):
        self.txCountry['values'], self.txCountryHidden['values']  = self.sofifa.get_countries()
        self.txCountry.current(0)
        self.txCountryHidden.current(0)

    def load_combo_player(self):
        nation = str(self.txCountryHidden.get())
        club = int(self.txClubHidden.get())
        min_ovr = str(self.txMinOvr.get())
        max_ovr = str(self.txMaxOvr.get())
        version = str(self.txVersionHidden.get())
        selection = self.txSearch.get().lower()
        player_name = str(self.txPlayerName.get()).replace(' ','%20')
        self.player_list = self.sofifa.get_players(selection, nation, club, min_ovr, max_ovr, version, player_name)

    def load_combo_club(self):
        nation = str(self.txCountryHidden.get())
        version = str(self.txVersionHidden.get())
        if(nation == 0):
            self.txClub['values'], self.txClubHidden['values'] = ('None', 'None'), (0, 0)
        else:
            self.txClub['values'], self.txClubHidden['values'] = self.sofifa.get_clubs(nation, version)
        self.txClub.current(0)
        self.txClubHidden.current(0)
        self.load_combo_player()
        self.__sort_player_list()

    ### COMMANDS ###
    def __on_select_game(self, event):
        index = self.txGame.current()
        self.txGameHidden.current(index)
        self.load_combo_version()
        self.load_combo_club()

    def __on_select_player(self, event):
        index = self.txPlayerList.selection()[0]
        curItem = self.txPlayerList.focus()
        loc_value = self.txPlayerList.set(curItem, column='name')
        self.__win.clipboard_clear()
        self.__win.clipboard_append(loc_value)
        self.txPlayerID.delete(0,END)
        self.txPlayerID.insert(0, index)

    def __sort_player_list(self):
        for item in self.txPlayerList.get_children():
            self.txPlayerList.delete(item)
            self.txPlayerID.delete(0,END)
        if(len(self.player_list) > 0):
            if(self.column_sort == 0):
                self.player_list.sort(key=lambda x:x[self.column_sort], reverse=True)
            else:
                self.player_list.sort(key=lambda x:x[self.column_sort], reverse=False)
            for player in self.player_list:
                self.txPlayerList.insert('', 'end', player[5], values=(player[0], player[1], player[4], player[3], player[2]))
            self.txPlayerList.selection_set(self.txPlayerList.get_children()[0])
            self.txPlayerID.insert(0, self.txPlayerList.selection()[0])
        else:
            self.txPlayerList.insert('', 'end', 0, values=(0,'Not found', 'None', 'None', 'None'))
    
    def __sort_tree_columns(self, column_index):
        self.__reset_tree_columns()
        self.column_sort = column_index
        if column_index == 0:
            self.txPlayerList.heading('bov', text='▲ OVR')
        elif column_index == 1:
            self.txPlayerList.heading('name', text='▼ NAME')
        elif column_index == 2:
            self.txPlayerList.heading('club', text='▼ CLUB')
        elif column_index == 3:
            self.txPlayerList.heading('pos', text='▼ POS')
        elif column_index == 4:
            self.txPlayerList.heading('nation', text='▼ NATION')
        self.__sort_player_list()

    def __on_select_clubs(self, event):
        index = self.txClub.current()
        self.txClubHidden.current(index)
        self.load_combo_player()
        self.__sort_player_list()

    def __on_select_version_country(self, event):
        index = self.txVersion.current()
        self.txVersionHidden.current(index)
        index = self.txCountry.current()
        self.txCountryHidden.current(index)
        self.load_combo_club()
        self.__on_select_clubs(event)

    def __binding_values(self):
        self.txGame.bind('<<ComboboxSelected>>', self.__on_select_game)
        self.txVersion.bind('<<ComboboxSelected>>', self.__on_select_version_country)
        self.txCountry.bind('<<ComboboxSelected>>', self.__on_select_version_country)
        self.txClub.bind('<<ComboboxSelected>>', self.__on_select_clubs)
        self.txSearch.bind('<<ComboboxSelected>>', self.__on_select_clubs)
        self.txMinOvr.bind('<<ComboboxSelected>>', self.__on_select_clubs)
        self.txMaxOvr.bind('<<ComboboxSelected>>', self.__on_select_clubs)
        self.txPlayerList.bind('<ButtonRelease-1>', self.__on_select_player)
        self.txPlayerName.bind('<Return>', self.__on_select_clubs)

    def __set_commands(self):
        self.btConvertClassic.config(command=self.__search_stats_classic)
        self.btConvert.config(command=self.__search_stats_online)
        self.btClipboard.config(command=self.__copy_to_clipboard)
        self.btAbout.config(command=self.__about_app)
        self.txPlayerList.heading('bov', command=lambda: self.__sort_tree_columns(0))
        self.txPlayerList.heading('name', command=lambda: self.__sort_tree_columns(1))
        self.txPlayerList.heading('club', command=lambda: self.__sort_tree_columns(2))
        self.txPlayerList.heading('pos', command=lambda: self.__sort_tree_columns(3))
        self.txPlayerList.heading('nation', command=lambda: self.__sort_tree_columns(4))

    # def __backup_stats(self):
    #     player = str(self.txPlayerID.get())
    #     version = str(self.txGameHidden.get())
    #     nation = str(self.txCountry.get())
    #     file_obj = open(f'statsdb/{nation}_{player}_{version}.txt', 'w')
    #     file_obj.write(str(self.__player_stats))
    #     file_obj.close()

    def __copy_to_clipboard(self):
        self.__win.clipboard_clear()
        self.__win.clipboard_append(str(self.__player_stats))

    def __search_stats_online(self):
        player = str(self.txPlayerID.get())
        if(player.isnumeric() == True):
            self.__player_stats = self.pes6es.convert_player(player)
            self.__copy_to_clipboard()
        else:
            tkm.showwarning(self.__appname, 'You must select a player first!')

    def __search_stats_classic(self):
        player = str(self.txPlayerID.get())
        version = str(self.txGameHidden.get())
        season = str(self.txVersion.get())
        season = str(season[len(season)-4:len(season)])
        json = self.sofifa.player_json(player, version, season)
        if(player.isnumeric() == True):
            self.__player_stats = self.pes6es.convert_offline(json)
            self.__copy_to_clipboard()
        else:
            tkm.showwarning(self.__appname, 'You must select a player first!')

    def __load_default_values(self):
        self.load_combo_game()
        self.load_combo_version()
        self.load_combo_country()
        self.txMinOvr['values'] = (60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99)
        self.txMinOvr.current(10)
        self.txMaxOvr['values'] = (60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99)
        self.txMaxOvr.current(END)
        self.txSearch['values'] = ('All', 'Updated', 'Removed', 'Free', 'Added')
        self.txSearch.current(0)
        self.load_combo_club()

    def main(self):
        self.__app_labels()
        self.__app_entries()
        self.__app_buttons()
        self.__app_config()
        self.__app_grid_config()
        self.__binding_values()
        self.__set_commands()
        self.__load_default_values()
        self.__win.protocol('WM_DELETE_WINDOW', self.__window_close)
        self.__win.mainloop()