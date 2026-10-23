import plistlib
import urllib.parse

def convert_phigros_plist_to_xml(plist_path, xml_output_path):
    # 1. Đọc file plist
    with open(plist_path, 'rb') as f:
        plist_data = plistlib.load(f)

    xml_lines = [
        "<?xml version='1.0' encoding='utf-8' standalone='yes' ?>",
        "<map>",
        '    <int name="__UNITY_PLAYERPREFS_VERSION__" value="1" />'
    ]

    # Danh sách các key đặc thù của riêng iOS cần bỏ qua
    ignore_keys = {'game_detail', 'device_id', 'TDSAchievement-DeviceId'}

    for key, val in plist_data.items():
        if key in ignore_keys or key.startswith('Apple') or key.startswith('NS'):
            continue

        # Mã hóa URL cho Key (%2B, %2F, %3D...) giống chuẩn Unity Android
        encoded_key = urllib.parse.quote(str(key), safe='')

        # Xử lý theo từng kiểu dữ liệu
        if isinstance(val, str):
            encoded_val = urllib.parse.quote(val, safe='')
            xml_lines.append(f'    <string name="{encoded_key}">{encoded_val}</string>')
        elif isinstance(val, bool):
            int_val = 1 if val else 0
            xml_lines.append(f'    <int name="{encoded_key}" value="{int_val}" />')
        elif isinstance(val, int):
            xml_lines.append(f'    <int name="{encoded_key}" value="{val}" />')
        elif isinstance(val, float):
            xml_lines.append(f'    <float name="{encoded_key}" value="{val}" />')
        # Tự động bỏ qua kiểu bytes (<data>) như 'game_detail'

    xml_lines.append("</map>")

    # 2. Ghi ra file XML hoàn chỉnh
    with open(xml_output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines) + '\n')

    print(f"converted! your save file is saved as: {xml_output_path} like lol what r u expecting")

# Chạy hàm chuyển đổi (Đổi tên file đầu vào đúng với tên file trên máy của bạn)
convert_phigros_plist_to_xml(
    plist_path='ios_save.plist', 
    xml_output_path='com.PigeonGames.Phigros.v2.playerprefs.xml'
)