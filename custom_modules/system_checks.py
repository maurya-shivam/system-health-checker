import psutil as ut
import platform as plt
import uuid, datetime, socket, ssl
import smtplib as smt
from email.message import EmailMessage
from sys import stdin

def line():
    return ''.join(['_' for x in range(150)])

def host():
    host = socket.gethostname()
    return '%s\nHostname: %s\n%s\n' %(line(), host, line())
    
def cpu():
    cpu_count = ut.cpu_count()
    cpu_freq = ut.cpu_freq()
    cpu_pertime = ut.cpu_times_percent()
    cpu_per = ut.cpu_percent()
    
    return ('CPU count: {}\nCPU Frequency:\n\tMax_freq: {} MHz\tCurrent_Freq: {} MHz\n\nCPU_usage:\n\tUser: {}%\tSystem: {}%\tInterrupt: {}%\t\tIdle:{}%\n\nTotal_CPU_percentage use: {}%\n{}'
          .format(cpu_count, cpu_freq.max, cpu_freq.current, cpu_pertime.user, 
                  cpu_pertime.system, cpu_pertime.interrupt, cpu_pertime.idle, cpu_per, line()))

def memory():
    mem = ut.virtual_memory()
    mem_total = mem.total/1e+6
    mem_used =  mem.used/1e+6
    mem_available =  mem.available/1e+6
    per_used =  mem.percent
    
    return ('System Memory:\n\n\tTotal_Memory: {} Mb\t\tUsed_Memory: {} Mb\t\tAvailable_Memory: {} Mb\t\tPercentage_Used: {}%\n{}\n'
          .format(mem_total, mem_used, mem_available, per_used, line()))
    
def disk():
    disk_part = ut.disk_partitions()
    disk_str = ''
    for dir in disk_part:
        disk = ut.disk_usage('%s' %dir.mountpoint)
        disk_str += ('Disk: {}\tType: {}\tTotal: {} Mb\t\tUsed: {} Mb\t\tFree: {} Mb\t\tPercent_Used: {}%\n'
              .format(dir.mountpoint, dir.fstype, disk.total/1e+6, disk.used/1e+6, disk.free/1e+6, disk.percent))
    return(disk_str)

def system():
    uname = plt.uname()
    platform = uname.system
    platform_type = uname.release
    version = uname.version
    device = uname.node
    processor = uname.processor
    return ('{} {}\tUpdate Version: {}\nDevice: {}\nCPU info: {}\n{}\n'.format(platform, platform_type, version, device, processor, line()))

def uid():
    uid = uuid.uuid4()
    return ('UUID: %s\n%s'%(uid, line()))

def date_time():
    date = datetime.datetime.now()
    return ('Data Retrived on: %s\n%s' %(date.strftime('%A, %d-%B-%Y, %H:%M:%S'), line()))

def msg_body():
    print("\nEnter your text here: (use  '/end'  to terminate):\n")
    msg = ''
    while True:
        line = stdin.readline()
        if not '/end' in line: msg += line
        else: break
    return msg