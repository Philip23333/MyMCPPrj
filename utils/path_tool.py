import os


def get_prj_root() -> str:
    """Get the absolute path of the project root directory."""
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 项目根目录假设为当前文件所在目录的上一级
    project_root = os.path.dirname(current_dir)
    return project_root

def get_abs_path(rel_path: str) -> str:
    """Convert a relative path to an absolute path based on the project root."""
    prj_root = get_prj_root()
    # 拼接项目根目录和相对路径，得到绝对路径
    abs_path = os.path.join(prj_root, rel_path)
    return abs_path




if __name__ == '__main__':
    # 测试函数
    test_rel_path = 'configs/agent.yml'
    print(get_abs_path(test_rel_path))