#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old executive summary block
old_block = """    <!-- FOLLOW-UP EXECUTIVE SUMMARY -->
    <section class="section">
      <div class="section-label">Executive summary — April's shipped winners</div>
      <div class="kpi-grid">
        <div class="kpi">
          <div class="kpi-label">Tests tracked</div>
          <div class="kpi-value" style="padding: 5px 0;">3</div>
          <div class="kpi-delta neutral">shipped in April, tracked in May</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Status</div>
          <div class="kpi-value" style="padding: 5px 0; font-size: 15px; line-height: 1.6;">
            <span style="color:#1D9E75;">1 ✓</span> &middot;
            <span style="color:#3B82F6;">1 📊</span> &middot;
            <span style="color:#F59E0B;">1 ✕</span>
          </div>
          <div class="kpi-delta neutral">holding · measured · removed</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Active revenue impact</div>
          <div class="kpi-value pos" style="padding: 5px 0;">৳80,269</div>
          <div class="kpi-delta neutral" style="padding-left: 3px;">/ month (Extra-discount books)</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Gross attributed</div>
          <div class="kpi-value" style="padding: 5px 0; color: var(--blue);">৳1,02,281</div>
          <div class="kpi-delta neutral">QuickDeal badge (no control arm)</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Captured Apr–May</div>
          <div class="kpi-value pos" style="padding: 5px 0;">৳1,00,336</div>
          <div class="kpi-delta neutral">Extra-discount books total</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Archived (not live)</div>
          <div class="kpi-value" style="padding: 5px 0; color: var(--text3);">৳58,669</div>
          <div class="kpi-delta neutral">Foreign book price (removed)</div>
        </div>
      </div>
    </section>"""

# Define the new executive summary block
new_block = """    <!-- FOLLOW-UP EXECUTIVE SUMMARY -->
    <section class="section">
      <div class="section-label">Executive summary — April's shipped winners</div>
      <div class="kpi-grid">
        <div class="kpi">
          <div class="kpi-label">Tests tracked</div>
          <div class="kpi-value" style="padding: 5px 0;">3</div>
          <div class="kpi-delta neutral">shipped in April, tracked in May</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Status</div>
          <div class="kpi-value" style="padding: 5px 0; font-size: 15px; line-height: 1.6;">
            <span style="color:#1D9E75;">1 ✓</span> &middot;
            <span style="color:#3B82F6;">1 📊</span> &middot;
            <span style="color:#F59E0B;">1 ✕</span>
          </div>
          <div class="kpi-delta neutral">holding · measured · removed</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Active revenue impact</div>
          <div class="kpi-value pos" style="padding: 5px 0;">৳1,82,550</div>
          <div class="kpi-delta neutral" style="padding-left: 3px;">/ month (Extra-discount + QuickDeal)</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Archived (not live)</div>
          <div class="kpi-value" style="padding: 5px 0; color: var(--text3);">৳58,669</div>
          <div class="kpi-delta neutral">Foreign book price (removed)</div>
        </div>
      </div>
    </section>"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Could not find the block to replace")
