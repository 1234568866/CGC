from PIL import Image
import os


def bmp_to_png(input_path: str, output_path: str) -> None:
    """
    将单张 BMP 图像无损转换为 PNG 并保存。

    参数:
        input_path (str): 输入 BMP 图像文件路径
        output_path (str): 输出 PNG 图像文件路径
    """
    # 打开 BMP 图像
    with Image.open(input_path) as img:
        # 确保是 BMP 格式
        if img.format != 'BMP':
            raise ValueError(f"输入文件不是 BMP 格式: {input_path}")
        # 保存为 PNG，PIL 默认为无损压缩
        img.save(output_path, format='PNG')


def batch_bmp_to_png(input_dir: str, output_dir: str) -> None:
    """
    批量将目录下的所有 BMP 图像转换为 PNG。

    参数:
        input_dir (str): 包含 BMP 文件的输入目录
        output_dir (str): 保存 PNG 文件的输出目录
    """
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        if fname.lower().endswith('.bmp'):
            bmp_path = os.path.join(input_dir, fname)
            png_name = os.path.splitext(fname)[0] + '.png'
            png_path = os.path.join(output_dir, png_name)
            try:
                bmp_to_png(bmp_path, png_path)
                print(f"转换成功: {bmp_path} → {png_path}")
            except Exception as e:
                print(f"转换失败: {bmp_path}，原因: {e}")


if __name__ == "__main__":
    # 示例用法
    input_directory = "path/to/bmp_images"
    output_directory = "path/to/png_images"
    batch_bmp_to_png(input_directory, output_directory)
