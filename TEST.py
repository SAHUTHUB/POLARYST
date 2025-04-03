import graphviz

dot = graphviz.Digraph('equity_research', comment='Equity Research Flowchart', graph_attr={'rankdir': 'TB'}) # TB = Top to Bottom

# Node styles
logo_node_attr = {'shape': 'plaintext', 'fontsize': '8', 'fontcolor': 'blue!50!black'} # node logo, แก้ไขสี font ที่นี่
    # ... nodes อื่นๆ ...
    dot.node('educba_logo', 'EDUCBA', **logo_node_attr) # บรรทัดนี้ไม่ต้องแก้
    # ... edges และส่วนอื่นๆ ...
input_node_attr = {'fillcolor': 'white'} # ปรับสี input node เป็นสีขาว
process_node_attr = {'fillcolor': 'white'} # ปรับสี process node เป็นสีขาว
output_node_attr = {'fillcolor': 'lightgreen'}
textbox_node_attr = {'shape': 'box', 'style': 'rounded', 'fillcolor': 'white', 'width': '2.5', 'height': '0.5', 'fontsize': '8'} # ปรับขนาดและ font textbox
small_node_attr = {'shape': 'box', 'style': 'rounded,filled', 'fillcolor': 'white', 'width': '0.5', 'height': '0.3', 'fontsize': '8'} # node เล็ก
logo_node_attr = {'shape': 'plaintext', 'fontsize': '8', 'fontcolor': 'blue'} # node logo

# Nodes
dot.node('analyst', 'Equity Research Analyst', **input_node_attr)
dot.node('stock', "Company A's Stock", **process_node_attr)
dot.node('financial_model', 'Financial Modeling', **process_node_attr)
dot.node('dcf_valuation', 'DCF Valuation', **process_node_attr)
dot.node('report', 'Equity Research Report', **output_node_attr)
dot.node('clients', 'Clients', **input_node_attr)
dot.node('client_desc', '(Pension & Mutual Funds,\nRetail Investors, Hedge Funds)', **textbox_node_attr)

# Decorative nodes
dot.node('number1000', '1000', **small_node_attr)
dot.node('dollar_sign', '$', **small_node_attr)
dot.node('compiles_text', 'Compiles Result\nto Create', shape='plaintext', fontsize='9', fontname='Arial', align='center') # plaintext shape สำหรับ text node
dot.node('performing_text_left', 'By Performing', shape='plaintext', fontsize='9', fontname='Arial', align='right')
dot.node('performing_text_right', 'By Performing', shape='plaintext', fontsize='9', fontname='Arial', align='left')
dot.node('used_by_text', 'Which is Used By', shape='plaintext', fontsize='9', fontname='Arial', align='left')
dot.node('s_node', 'S', **small_node_attr)
dot.node('one_node', '1', **small_node_attr)
dot.node('zerozerozero_node', '000', **small_node_attr)
dot.node('educba_logo', 'EDUCBA', **logo_node_attr, fontcolor='blue!50!black')


# Edges (Arrows)
dot.edge('analyst', 'stock', label='Analyzes', arrowhead='vee', style='bold')
dot.edge('stock', 'financial_model', label='By Performing', labeldistance=1.2, labelposition='l', arrowhead='vee', style='bold')
dot.edge('stock', 'dcf_valuation', label='By Performing', labeldistance=1.2, labelposition='r', arrowhead='vee', style='bold')
dot.edge('financial_model', 'report', taillabel=' ', headlabel=' ', xlabel='Compiles Result\nto Create',  arrowhead='vee', style='bold', to_port='w', tail_port='s', minlen='2') # ปรับแต่ง edge ไป report
dot.edge('dcf_valuation', 'report', taillabel=' ', headlabel=' ', arrowhead='vee', style='bold', to_port='e', tail_port='s', minlen='2') # ปรับแต่ง edge ไป report
dot.edge('report', 'clients', label='Which is Used By', arrowhead='vee', style='bold')
dot.edge('clients', 'client_desc', arrowhead='vee', style='bold')

# Positioning (จัดตำแหน่ง - ใช้ subgraph เพื่อจัดกลุ่ม node)
with dot.subgraph(name='cluster_analyst_stock') as c:
    c.attr(rank='same') # จัด analyst และ stock ให้อยู่ระดับเดียวกัน
    c.node('analyst')
    c.node('stock')

with dot.subgraph(name='cluster_valuation') as c_val:
    c_val.attr(rank='same') # จัด financial_model และ dcf_valuation ให้อยู่ระดับเดียวกัน
    c_val.node('financial_model')
    c_val.node('dcf_valuation')


# Add decorative nodes - positioning relative to main nodes
dot.edge('number1000', 'analyst', style='invis', constraint='false') # node 1000 ไว้เหนือ analyst
dot.edge('analyst', 'dollar_sign', style='invis', constraint='false') # dollar sign ไว้เหนือ stock
dot.edge('report', 'compiles_text', style='invis', constraint='false') # compiles_text ไว้เหนือ report
dot.edge('financial_model', 'performing_text_left', style='invis', constraint='false') # performing_text_left ไว้ข้าง financial_model
dot.edge('dcf_valuation', 'performing_text_right', style='invis', constraint='false') # performing_text_right ไว้ข้าง dcf_valuation
dot.edge('clients', 'used_by_text', style='invis', constraint='false') # used_by_text ไว้ข้าง clients
dot.edge('report', 's_node', style='invis', constraint='false') # s_node ข้าง report
dot.edge('report', 'one_node', style='invis', constraint='false') # one_node ข้าง report
dot.edge('report', 'zerozerozero_node', style='invis', constraint='false') # zerozerozero_node ข้าง report
dot.edge('report', 'educba_logo', style='invis', constraint='false') # educba_logo ข้าง report


# Output to file (สร้างไฟล์ output)
dot.render('equity_research_flowchart', format='png', view=False) # บันทึกเป็นไฟล์ PNG, ไม่เปิด preview อัตโนมัติ


print("Flowchart 'equity_research_flowchart.png' created successfully!")