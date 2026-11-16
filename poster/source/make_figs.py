import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'Liberation Sans','font.size':21,'axes.spines.top':False,'axes.spines.right':False,
  'axes.linewidth':1.4,'xtick.major.width':1.4,'ytick.major.width':1.4,'axes.titleweight':'bold','axes.titlesize':23,'axes.labelsize':21,'xtick.labelsize':20,'ytick.labelsize':20,'figure.dpi':100})
G='#2f7a36'; GREY='#8c9aa3'; GOLD='#d9a92a'; RED='#b33a2f'
def save(fig,name):
    fig.savefig(f'assets/fig/{name}.png',dpi=300,bbox_inches='tight',facecolor='white'); plt.close(fig)

# Fig 1: lifelong (genetic) vs trial LDL-C lowering, per 1 mmol/L
fig,ax=plt.subplots(figsize=(15.5,6.2))
labels=['Statin trials\n(~5 years of treatment)\nCTT 2010','Lifelong lower LDL-C\n(genetic variants)\nFerence 2012']
vals=[22,54.5]; lo=[20,48.8]; hi=[24,59.5]
err=[[v-l for v,l in zip(vals,lo)],[h-v for v,h in zip(vals,hi)]]
bars=ax.bar(labels,vals,color=[GREY,G],width=0.55,yerr=err,capsize=8,error_kw={'elinewidth':1.8,'ecolor':'black'})
for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v+5,f'{v:g}%',ha='center',va='bottom',fontweight='bold',fontsize=22)
ax.set_ylabel('Reduction in coronary heart disease risk\nper 1 mmol/L lower LDL-C (%)')
ax.set_ylim(0,72); ax.set_yticks(range(0,71,10))
ax.set_title('The earlier and longer LDL-C is lowered, the larger the benefit')
ax.text(0.0,-0.30,'Error bars: 95% CI. Sources: Cholesterol Treatment Trialists’ Collaboration, Lancet 2010 (RR 0.78 per mmol/L, 170,000 participants); Ference et al., JACC 2012 (Mendelian randomisation, 312,321 participants).',transform=ax.transAxes,fontsize=15,color='#444',wrap=True)
save(fig,'exposure')

# Fig 2: forest plot, Chambari 2026, mg/dL outcomes
fig,ax=plt.subplots(figsize=(9.6,5.6))
rows=[('LDL-C',-39.5,-53.5,-25.6),('Total cholesterol',-44.7,-62.0,-27.4),('Triglycerides',-52.5,-66.1,-38.9),('Fasting glucose',-12.1,-17.1,-7.2),('HDL-C',5.6,3.8,7.5)]
y=np.arange(len(rows))[::-1]
for yi,(n,m,l,h) in zip(y,rows):
    ax.plot([l,h],[yi,yi],color='black',lw=1.4); ax.plot([l,l],[yi-0.15,yi+0.15],color='black',lw=1.2); ax.plot([h,h],[yi-0.15,yi+0.15],color='black',lw=1.2)
    ax.plot(m,yi,marker='s',ms=13,color=G if m<0 else GOLD,mec='black',mew=0.8)
    ax.text(12,yi,f'{m:+.1f} ({l:.1f} to {h:.1f})',va='center',fontsize=19)
ax.axvline(0,color=RED,lw=1.2,ls='--')
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows],fontweight='bold')
ax.set_xlim(-75,70); ax.set_xlabel('Mean difference vs control (mg/dL)')
ax.set_ylim(-0.8,len(rows)-0.3)
ax.text(14,len(rows)-0.55,'MD (95% CI)',fontsize=17,fontweight='bold')
ax.text(-72,-0.62,'◄ favours bergamot',fontsize=17,color=G)
ax.set_title('Bergamot vs control: pooled effects in adults (9 RCTs, n = 615)',pad=10)
save(fig,'forest')

# Fig 3: LDL-C reduction across meta-analyses
fig,ax=plt.subplots(figsize=(4.6,5.6))
names=['Sadeghi\n2022','Chambari\n2026','Osadnik\n2022']
vals=[55,39.5,47]
bars=ax.bar(names,vals,color=G,width=0.6)
ax.errorbar([1],[39.5],yerr=[[39.5-25.6],[53.5-39.5]],fmt='none',ecolor='black',capsize=8,elinewidth=1.8)
for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v+(15 if v==39.5 else 1.5),f'−{v:g}',ha='center',va='bottom',fontweight='bold',fontsize=21)
ax.set_ylabel('LDL-C reduction (mg/dL)'); ax.set_ylim(0,70)
ax.set_title('LDL-C lowering,\nmeta-analyses',pad=10)
ax.text(0,-0.26,'14 trials; 9 RCTs; network MA. 95% CI where reported.',transform=ax.transAxes,fontsize=15,color='#444')
save(fig,'meta')

# Fig 4: Ferro 2020 liver fat (CAP) change
fig,ax=plt.subplots(figsize=(4.6,5.6))
grp=['Bergamot\n(n = 50)','Placebo\n(n = 52)']; vals=[-48,-27]
bars=ax.bar(grp,vals,color=[GOLD,GREY],width=0.55)
for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v-2,f'{v}',ha='center',va='top',fontweight='bold',fontsize=22)
ax.axhline(0,color='black',lw=1)
ax.set_ylabel('Change in CAP at 12 wk (dB/m)'); ax.set_ylim(-62,5)
ax.set_title('Liver fat (CAP),\nFerro 2020',pad=10)
ax.text(0,-0.30,'CAP: controlled attenuation parameter; n = 102.',transform=ax.transAxes,fontsize=15,color='#444')
save(fig,'liver')

# Fig 5: trials by population
fig,ax=plt.subplots(figsize=(13,5.4))
pops=['Young patients','Fatty liver','Type 2 diabetes','Overweight /\nmetabolic syndrome','High cholesterol']
n=[0,1,1,2,3]; cols=[RED,G,G,G,G]
bars=ax.barh(pops,n,color=cols,height=0.6)
for b,v in zip(bars,n): ax.text(v+0.08,b.get_y()+b.get_height()/2,str(v),va='center',fontweight='bold',fontsize=22)
ax.set_xlim(0,3.8); ax.set_xticks([0,1,2,3]); ax.set_xlabel('Number of key randomised trials')
ax.set_title('Seven key bergamot RCTs by study population')
src=['','Ferro 2020','Mollace','Capomolla; Rondanelli','Gliozzi 2013; Fogacci; Stonehouse 2025']
for i,(b,s) in enumerate(zip(bars,src)):
    if s: ax.text(0.08,b.get_y()+b.get_height()/2,s,va='center',fontsize=16,color='white')
save(fig,'pop')
print('ok')
