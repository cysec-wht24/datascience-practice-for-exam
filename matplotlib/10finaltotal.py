import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
x   = np.linspace(0, 2 * np.pi, 100)
x3d = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x3d, x3d)
Z    = np.sin(np.sqrt(X**2 + Y**2))

categories = ['Math', 'Science', 'English', 'History']
scores     = [85, 90, 78, 88]
rng_data   = [np.random.randn(80) for _ in range(3)]

# ── Style & Layout ────────────────────────────────────────────────────────────
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(16, 12))
fig.suptitle(r'$Matplotlib\ Concepts\ Demo$', fontsize=16, fontweight='bold')
fig.patch.set_facecolor('#F5F5F5')

# ── 1. Line Plot ──────────────────────────────────────────────────────────────
ax1 = fig.add_subplot(3, 3, 1)
ax1.plot(x, np.sin(x), color='#2196F3', lw=2, linestyle='--', marker='o',
         markersize=3, markerfacecolor='red', label='sin(x)')
ax1.plot(x, np.cos(x), color='#F44336', lw=2, label='cos(x)')
ax1.set_xlim(0, 2*np.pi)
ax1.set_ylim(-1.5, 1.5)
ax1.set_title('Line Plot', fontweight='bold')
ax1.set_xlabel(r'$\theta$ (rad)')
ax1.set_ylabel('Amplitude')
ax1.legend(loc='upper right', fontsize=8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax1.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
ax1.tick_params(axis='x', rotation=30)
ax1.grid(True, linestyle='--', alpha=0.5)

# ── 2. Scatter Plot ───────────────────────────────────────────────────────────
ax2 = fig.add_subplot(3, 3, 2)
sx, sy = np.random.randn(80), np.random.randn(80)
colors = np.sqrt(sx**2 + sy**2)
sc = ax2.scatter(sx, sy, c=colors, cmap='viridis', alpha=0.7, edgecolors='black', lw=0.3)
fig.colorbar(sc, ax=ax2, label='Distance')
ax2.set_title('Scatter Plot', fontweight='bold')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

# ── 3. Bar + Annotations ──────────────────────────────────────────────────────
ax3 = fig.add_subplot(3, 3, 3)
bars = ax3.bar(categories, scores, color=['#2196F3','#4CAF50','#F44336','#FF9800'])
ax3.set_title('Bar Plot', fontweight='bold')
ax3.set_ylabel('Score')
ax3.set_ylim(0, 110)
for bar, score in zip(bars, scores):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(score), ha='center', va='bottom', fontsize=9)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# ── 4. Histogram ──────────────────────────────────────────────────────────────
ax4 = fig.add_subplot(3, 3, 4)
data = np.random.randn(500)
ax4.hist(data, bins=25, color='steelblue', edgecolor='black', alpha=0.7, density=True)
ax4.set_title('Histogram', fontweight='bold')
ax4.set_xlabel('Value')
ax4.set_ylabel('Density')

# ── 5. Box Plot ───────────────────────────────────────────────────────────────
ax5 = fig.add_subplot(3, 3, 5)
ax5.boxplot(rng_data, tick_labels=['G1', 'G2', 'G3'])
ax5.set_title('Box Plot', fontweight='bold')
ax5.set_ylabel('Values')

# ── 6. Annotate + Shapes ──────────────────────────────────────────────────────
ax6 = fig.add_subplot(3, 3, 6)
ax6.plot(x, np.sin(x), color='teal', lw=2)
ax6.annotate('Peak', xy=(np.pi/2, 1), xytext=(np.pi, 0.6),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=10, color='blue')
ax6.text(4, -0.8, r'$\sin(\theta)$', fontsize=10, color='red', fontweight='bold',
         bbox=dict(facecolor='lightyellow', edgecolor='red', boxstyle='round'))
rect = mpatches.Rectangle((4.5, -0.4), 1.2, 0.8, linewidth=1,
                            edgecolor='purple', facecolor='none', linestyle='--')
ax6.add_patch(rect)
ax6.set_title('Annotations & Shapes', fontweight='bold')
ax6.set_xlim(0, 2*np.pi)

# ── 7. Log Scale ──────────────────────────────────────────────────────────────
ax7 = fig.add_subplot(3, 3, 7)
t = np.linspace(0.1, 10, 200)
ax7.plot(t, np.exp(t), color='darkgreen', lw=2)
ax7.set_yscale('log')
ax7.set_title('Log Scale (Y)', fontweight='bold')
ax7.set_xlabel('X')
ax7.set_ylabel(r'$e^x$ (log)')
ax7.grid(True, which='both', linestyle='--', alpha=0.4)

# ── 8. 3D Surface ─────────────────────────────────────────────────────────────
ax8 = fig.add_subplot(3, 3, 8, projection='3d')
surf = ax8.plot_surface(X, Y, Z, cmap='plasma', alpha=0.85)
fig.colorbar(surf, ax=ax8, shrink=0.5, label='Z')
ax8.set_title('3D Surface', fontweight='bold')
ax8.view_init(elev=30, azim=45)
ax8.set_xlabel('X'); ax8.set_ylabel('Y'); ax8.set_zlabel('Z')

# ── 9. 3D Scatter ─────────────────────────────────────────────────────────────
ax9 = fig.add_subplot(3, 3, 9, projection='3d')
xs, ys, zs = np.random.randn(60), np.random.randn(60), np.random.randn(60)
ax9.scatter(xs, ys, zs, c=zs, cmap='cool', s=40)
ax9.set_title('3D Scatter', fontweight='bold')
ax9.view_init(elev=20, azim=60)

# ── Save & Show ───────────────────────────────────────────────────────────────
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('matplotlib_all_concepts.png', dpi=150, bbox_inches='tight', facecolor='#F5F5F5')
plt.show()