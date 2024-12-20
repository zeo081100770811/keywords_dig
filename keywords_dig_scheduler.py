#!/usr/bin/env python3
import sys
import os
import logging
from datetime import datetime
from keywords_dig import SemrushCrawler

# 设置日志
def setup_logging():
    # 创建日志目录
    log_dir = os.path.join(os.path.expanduser('~'), 'logs', 'keywords_dig')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 设置日志文件名（包含日期）
    log_file = os.path.join(log_dir, f'keywords_dig_{datetime.now().strftime("%Y%m%d")}.log')
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    try:
        # 设置日志
        setup_logging()
        
        # 记录开始时间
        logging.info("开始执行关键词挖掘任务")
        start_time = datetime.now()
        
        # 创建爬虫实例并执行
        crawler = SemrushCrawler()
        crawler.start()
        
        # 记录结束时间和执行时长
        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"任务执行完成，总耗时: {duration}")
        
    except Exception as e:
        logging.error(f"执行过程中发生错误: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
