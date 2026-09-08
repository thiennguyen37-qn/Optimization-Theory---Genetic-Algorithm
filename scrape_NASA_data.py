"""Tải dữ liệu NASA dùng trong NASA.ipynb về thư mục data/.

Chạy trực tiếp: python scrape_NASA_data.py
"""

import requests
import pandas as pd
from io import StringIO

CDAWEB_BASE_URL = "https://cdaweb.gsfc.nasa.gov/hapi"


def scrape_wind_solar_wind(output_path="data/NASA_WIND_solar_wind.csv"):
    """Tải dữ liệu plasma/từ trường của vệ tinh WIND từ NASA CDAWeb HAPI."""

    # Dataset thật của vệ tinh WIND đặt tên "WI_..." hoặc "WIND_..." — lọc
    # theo TIỀN TỐ thay vì substring "WIND" (substring bắt nhầm cả
    # TOOWINDY_*, DE2_WIND2S_WATS, ...*SOLAR-WIND của vệ tinh KHÁC, đồng
    # thời bỏ sót phần lớn dataset WIND thật dùng tiền tố viết tắt "WI_").
    catalog = requests.get(f"{CDAWEB_BASE_URL}/catalog").json()
    wind_datasets = [
        item["id"]
        for item in catalog["catalog"]
        if item["id"].upper().startswith(("WI_", "WIND_"))
    ]
    print(f"Found {len(wind_datasets)} WIND datasets.")

    # Chọn thẳng WI_H1_SWE (Solar Wind Experiment, thông số plasma
    # proton/alpha), phủ 1994-11-17 đến nay, chắc chắn có dữ liệu cho
    # khoảng thời gian bên dưới — không lấy wind_datasets[0] vì đó chỉ
    # là dataset đầu tiên theo thứ tự bảng chữ cái.
    dataset_id = "WI_H1_SWE"
    print("Selected dataset:", dataset_id)

    # Chỉ lấy vài thông số plasma chính (thay vì cả 86 cột) — vừa nhanh
    # hơn, vừa đỡ phải đoán tên cột sau khi nhận CSV không có header.
    data_parameters = ["Time", "Proton_V_nonlin", "Proton_Np_nonlin", "BX", "BY", "BZ"]

    response = requests.get(
        f"{CDAWEB_BASE_URL}/data",
        params={
            "id": dataset_id,
            "parameters": ",".join(data_parameters),
            "time.min": "2020-01-01T00:00:00Z",
            "time.max": "2020-01-07T00:00:00Z",
            "format": "csv",
        },
    )
    response.raise_for_status()

    # HAPI trả JSON (không phải CSV) khi có lỗi/không có dữ liệu, dù đã
    # xin format=csv — kiểm tra trước, không parse mù thành DataFrame.
    noi_dung = response.text.strip()
    if noi_dung.startswith("{"):
        raise RuntimeError(f"HAPI báo lỗi thay vì trả dữ liệu:\n{noi_dung}")

    # CSV trả về KHÔNG có header — tự đặt tên cột theo đúng data_parameters.
    df = pd.read_csv(StringIO(noi_dung), header=None, names=data_parameters)

    df.to_csv(output_path, index=False)
    print(f"WIND solar wind: {df.shape} -> {output_path}")
    return df


if __name__ == "__main__":
    scrape_wind_solar_wind()
