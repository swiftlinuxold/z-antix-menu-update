#!/usr/bin/python

# This is a revised version of the icemenuyap2.py Python program used by antiX Linux.

# -*- coding: utf-8 -*-
#
#    Build icewm menu from .desktop files in /usr/share/applications
#
#    Usage:   python icemenuyap2.py > icemenu.txt
#                or add to icewm startup file:
#                   python ~/.icewm/icemenuyap2.py > ~/.icewm/application &
#                and to icewm menu file:
#                   menufile "Application" "folder" ~/.icewm/application
#
#    Copyright (C) 2009  Federico Pelloni <federico.pelloni@gmail.com>
#                               Lion1810 <lion1810@inwind.it>
#    Based on icemenuyap.py by btekbas@gmail.com - which was based
#    on gnome2fluxmenu 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# To learn more about an imported module, import the module and enter its name.  
# Example: import os;os
# os module: from /usr/lib/python2.6, improves portability across platforms
# sys modeule: built-in, used for controlling parameters in the runtime environment
# random module: from /usr/lib/python2.6, generates random variables
# mimetypes module: from /usr/lib/python2.6, determines the MIME type given a path name
# glob module: from /usr/lib/python2.6, returns a list of all files in a directory with a 
# specific pattern
import os,sys,random,mimetypes,glob

gnmp_st="/usr/share/applications"


cat_sl_av=[]
cat_sl_devel=[]
cat_sl_edu=[]
catgrap_sl=[]
catnetw_sl=[]
catoffi_sl=[]
catothe_sl=[]
catdeve_sl=[]
catauvd_sl=[]
catsyst_sl=[]
catsysp_sl=[]
catsysa_sl=[]

cat_list_av=      1
cat_sl_devel=   1
cat_sl_edu=     1
cat_sl_elec=    1
cat_sl_eng=     1
catswc_game=    1
catswc_gra=     1
catswc_ham=     1
catswc_net=     1
catswc_of=      1
catswc_set=     1
catswc_sys=     1
catswc_util=    1

  if cate_st.find("AudioVideo")>0:   catswc_av+=      1
        if cate_st.find("Development")>0:  catswc_devel+=   1
        if cate_st.find("Education")>0:    catswc_edu+=     1
        if cate_st.find("Electronics")>0:  catswc_elec+=    1
        if cate_st.find("Engineering")>0:  catswc_eng+=     1
        if cate_st.find("Game")>0:         catswc_game+=    1
	    if cate_st.find("Graphics")>0:     catswc_gra+=     1
        if cate_st.find("HamRadio")>0:     catswc_ham+=     1
        if cate_st.find("Network")>0:      catswc_net+=     1
        if cate_st.find("Office")>0:       catswc_of+=      1
        if cate_st.find("Settings")>0:     catswc_set+=     1
        if cate_st.find("System")>0:       catswc_sys+=     1
	    if cate_st.find("Utility")>0:      catswc_util+=    1

cntacce=0;cntutil=0;cntgame=0;cntgrap=0;cntnetw=0;cntoffi=0
cntothe=0;cntdeve=0;cntauvd=0;cntsyst=0;cntsysp=0;cntsysa=0



# diritems_sl: list of all *.desktop files in the /usr/share/applications directory
diritems_sl = glob.glob(os.path.join(gnmp_st, "*.desktop"))

# diritems_sl: add any additional *.desktop files in a subdirectory within /usr/share/applications
diritems_sl += glob.glob(os.path.join(gnmp_st, "*", "*.desktop"))
for item in diritems_sl: # Proceed through all of the /usr/share/applications/* files
  # finp_st: each individual item within diritems_sl (each individual *.desktop file)
  finp_st=os.path.join(gnmp_st,item)
  
  if finp_st.endswith(".desktop"):
    finp_fl=open(finp_st,"r") # Read the *.desktop file
    cate_st="";name_st="";exec_st="";catswc=0
    catswc=0
    catswc_av=0 # AudioVideo
    catswc_devel=0 # Development
    catswc_edu=0 # Education
    catswc_elec=0 # Electronics
    catswc_eng=0 # Engineering
    catswc_game=0 # Game
    catswc_gra=0 # Graphics
    catswc_ham=0 # HamRadio
    catswc_net=0 # Network
    catswc_of=0 # Office
    catswc_set=0 # Settings
    catswc_sys=0 # System
    catswc_util=0 # Utility    
    
    # For each *.desktop file, set the value of the skip variable to False by default.
    skip=False
    while True:
      text_st=finp_fl.readline() # text_st is the line being read in the *.desktop file
      if len(text_st)==0:break # If there are no lines left to read, exit this "while True:" loop
      text_st=text_st.replace("\n","") # Remove the newline characters.
      if text_st.startswith("NoDisplay=true"):
	  # If the *.desktop file contains "NoDisplay=true", then set the value of skip to true.
        skip=True
      if text_st.startswith("Categories="):
        # Each category is worth a certain number of points for catswc.
        # If the *.desktop file fits multiple categories, the point values add up.
        cate_st=text_st

        # catswc_nota=0 # None of the above

        if cate_st.find("AudioVideo")>0:   catswc_av+=      1
        if cate_st.find("Development")>0:  catswc_devel+=   1
        if cate_st.find("Education")>0:    catswc_edu+=     1
        if cate_st.find("Electronics")>0:  catswc_elec+=    1
        if cate_st.find("Engineering")>0:  catswc_eng+=     1
        if cate_st.find("Game")>0:         catswc_game+=    1
	    if cate_st.find("Graphics")>0:     catswc_gra+=     1
        if cate_st.find("HamRadio")>0:     catswc_ham+=     1
        if cate_st.find("Network")>0:      catswc_net+=     1
        if cate_st.find("Office")>0:       catswc_of+=      1
        if cate_st.find("Settings")>0:     catswc_set+=     1
        if cate_st.find("System")>0:       catswc_sys+=     1
	    if cate_st.find("Utility")>0:      catswc_util+=    1
	    catswc_total=0
        catswc_total+=catswc_av+catswc_devel+catswc_edu+catswc_elec+catswc_eng
        catswc_total+=catswc_game+catswc_gra+catswc_ham+catswc_net+catswc_of
        catswc_total+=catswc_set+catswc_sys+catswc_util
	
      if text_st.startswith("Name="):
	    # In the "Name=" entry, replace ")" with "\\".
        name_st=text_st[5:];name_st=name_st.replace(")","\\)")
      if text_st.startswith("Icon="):
	icon_st=text_st[5:]
      if text_st.startswith("Exec="):
        if text_st.find('%') == -1:
        	exec_st=text_st[5:]
        else:
        	exec_st=text_st[5:text_st.find('%')-1]
    if skip: continue
    icepr_st="prog "+"\""+name_st+"\""+" "+"\""+icon_st+"\""+" "+exec_st


    if (catswc&   1)==  1:
      catacce_sl.append(icepr_st)
    if (catswc&   2)==  2:
      catutil_sl.append(icepr_st)
    if (catswc&   4)==  4:
      catgame_sl.append(icepr_st)
    if (catswc&   8)==  8:
      catgrap_sl.append(icepr_st)
    if (catswc&  16)== 16:
      catnetw_sl.append(icepr_st)
    if (catswc&  32)== 32:
      catoffi_sl.append(icepr_st)
    if (catswc&1023)==  0:
      catothe_sl.append(icepr_st)
    if (catswc&  64)== 64:
      catdeve_sl.append(icepr_st)
    if (catswc& 128)==128:
      catauvd_sl.append(icepr_st)
    if (catswc& 768)==256:
      catsyst_sl.append(icepr_st)
    if (catswc& 768)==512:
      catsysp_sl.append(icepr_st)
    if (catswc& 768)==768:
      catsysa_sl.append(icepr_st)


    finp_fl.close()
print"  menu \"Accessories\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-accessories.png {"
for i in catutil_sl: print"    "+i
for i in catacce_sl: print"    "+i
print"  }";print"  menu \"Development\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-development.png {"
for i in catdeve_sl: print"    "+i
print"  }";print"  menu \"Games\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-games.png {"
for i in catgame_sl: print"    "+i
print"  }";print"  menu \"Graphics\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-graphics.png {"
for i in catgrap_sl: print"    "+i
print"  }";print"  menu \"Multimedia\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-multimedia.png {"
for i in catauvd_sl: print"    "+i
print"  }";print"  menu \"Network\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-internet.png {"
for i in catnetw_sl: print"    "+i
print"  }";print"  menu \"Office\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-office.png {"
print"  prog \"Calculator\" /usr/share/icons/gTangish-2.0a1/32x32/apps/accessories-calculator.png xcalc"
for i in catoffi_sl: print"    "+i
print"  }";print"  menu \"Other\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-other.png {"
for i in catothe_sl: print"    "+i
print"  }";print"  menu \"System Prefs\" /usr/share/icons/gTangish-2.0a1/32x32/categories/preferences-system.png {"
for i in catsysp_sl: print"    "+i
print"  }";print"  menu \"System Tools\" /usr/share/icons/gTangish-2.0a1/32x32/categories/applications-system.png {"
for i in catsyst_sl: print"    "+i
for i in catsysa_sl: print"    "+i
print"}"
