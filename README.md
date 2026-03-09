
# Suspension Milling Visualization

Task 1 – Python for Industrial Automation

Visualization of particle size distribution (PSD) of a suspension **before and after milling** using Python, Pandas, Seaborn and Matplotlib.

---

# Repo structure

data/
    psd_raw_data.csv; 
    psd_raw_data.xlsx

src/
    visualize_psd.py;
    animate_psd.py

requirements.txt

README.md

---

# Run

Static visualization:

python src/visualize_psd.py

Animated transition (before → after milling):

python src/animate_psd.py

---

# Description

The scripts:

1. Load particle size distribution measurements
2. Compute mean volume fraction from three measurements
3. Plot PSD on a logarithmic particle diameter axis
4. Visualize the effect of milling

Two visualization modes are included:

- **Static PSD comparison**
- **Animated transition (crude → milled suspension)**

