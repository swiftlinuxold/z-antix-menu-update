#!/usr/bin/python
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
import os,sys,random,mimetypes,glob
gnmp_st="/usr/share/applications"
catacce_sl=[]
catutil_sl=[]
catgame_sl=[]
catgrap_sl=[]
catnetw_sl=[]
catoffi_sl=[]
catothe_sl=[]
catdeve_sl=[]
catauvd_sl=[]
catsyst_sl=[]
catsysp_sl=[]
catsysa_sl=[]
cntacce=0;cntutil=0;cntgame=0;cntgrap=0;cntnetw=0;cntoffi=0
cntothe=0;cntdeve=0;cntauvd=0;cntsyst=0;cntsysp=0;cntsysa=0
diritems_sl = glob.glob(os.path.join(gnmp_st, "*.desktop"))
diritems_sl += glob.glob(os.path.join(gnmp_st, "*", "*.desktop"))
for item in diritems_sl:
  finp_st=os.path.join(gnmp_st,item)
  if finp_st.endswith(".desktop"):
    finp_fl=open(finp_st,"r")
    cate_st="";name_st="";exec_st="";catswc=0
    catswc=0
    skip=False
    while True:
      text_st=finp_fl.readline()
      if len(text_st)==0:break
      text_st=text_st.replace("\n","")
      if text_st.startswith("NoDisplay=true"):
        skip=True
      if text_st.startswith("Categories="):
        cate_st=text_st
        if cate_st.find("Accessibility")>0:catswc+=   1
        if cate_st.find("Utility")>0:      catswc+=   2
        if cate_st.find("Game")>0:         catswc+=   4
        if cate_st.find("Graphics")>0:     catswc+=   8
        if cate_st.find("Network")>0:      catswc+=  16
        if cate_st.find("Office")>0:       catswc+=  32
        if cate_st.find("Development")>0:  catswc+=  64
        if cate_st.find("AudioVideo")>0:   catswc+= 128
        if cate_st.find("System")>0:       catswc+= 256
        if cate_st.find("Settings")>0:     catswc+= 512
        if cate_st.find("Core")>0:         catswc+=1024
      if text_st.startswith("Name="):
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
