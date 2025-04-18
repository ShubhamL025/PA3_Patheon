import sys
import matplotlib.pyplot as plt
import csv

def parse_log(log_file):
    times, sizes = [], []
    with open(log_file, 'r') as f:
        for line in f:
            if line.startswith('#') or '+' not in line:
                continue
            parts = line.strip().split('+')
            if len(parts) != 2:
                continue
            try:
                timestamp = int(parts[0].strip())
                size = int(parts[1].strip())
                times.append(timestamp)
                sizes.append(size)
            except ValueError:
                continue
    return times, sizes

def calculate_throughput(times, sizes):
    throughput_per_second = {}
    start_time = int(min(times)) // 1000
    for t, s in zip(times, sizes):
        second = (int(t) // 1000) - start_time
        throughput_per_second[second] = throughput_per_second.get(second, 0) + s
    return throughput_per_second

def calculate_rtt(log_file):
    rtts = []
    with open(log_file, 'r') as f:
        for line in f:
            if line.startswith('#') or '+' not in line:
                continue
            try:
                parts = line.strip().split('+')
                rtts.append(int(parts[0].strip()))
            except ValueError:
                continue
    if not rtts:
        return 0
    return sum(rtts) / len(rtts)

def calculate_loss_rate(sizes):
    # Assume each packet is a fixed size, so loss can't be determined directly
    # This is a placeholder — real loss needs extra packet sequence data
    return 0.0

def save_to_csv(throughput, avg_rtt, loss_rate, prefix):
    with open(f'{prefix}_throughput.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Time (s)', 'Throughput (Mbps)'])
        for second, bytes_sent in sorted(throughput.items()):
            mbps = (bytes_sent * 8) / 1e6
            writer.writerow([second, f"{mbps:.2f}"])

    with open(f'{prefix}_stats.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Metric', 'Value'])
        writer.writerow(['Average RTT (ms)', round(avg_rtt / 1000.0, 2)])
        writer.writerow(['Loss Rate', loss_rate])

def plot_throughput(throughput, prefix):
    x = sorted(throughput.keys())
    y = [(throughput[t] * 8) / 1e6 for t in x]
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xlabel('Time (s)')
    plt.ylabel('Throughput (Mbps)')
    plt.title(f'Throughput Over Time - {prefix.upper()}')
    plt.grid(True)
    plt.savefig(f'{prefix}_throughput.png')

def main():
    if len(sys.argv) != 3:
        print("Usage: python analyze_logs.py <datalink_log> <acklink_log>")
        return

    datalink_log = sys.argv[1]
    acklink_log = sys.argv[2]
    prefix = datalink_log.split('/')[-1].split('_')[0]  # e.g., vegas

    times, sizes = parse_log(datalink_log)
    throughput = calculate_throughput(times, sizes)
    avg_rtt = calculate_rtt(acklink_log)
    loss_rate = calculate_loss_rate(sizes)

    save_to_csv(throughput, avg_rtt, loss_rate, prefix)
    plot_throughput(throughput, prefix)
    print(f" Done: Saved CSV and PNG files for '{prefix}'.")

if __name__ == '__main__':
    main()
