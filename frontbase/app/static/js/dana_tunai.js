    document.addEventListener('DOMContentLoaded', function () {
        // Fungsi untuk memformat angka menjadi format mata uang Rupiah
        function formatRupiah(angka) {
            var number_string = angka.toString();
            var sisa = number_string.length % 3;
            var rupiah = number_string.substr(0, sisa);
            var ribuan = number_string.substr(sisa).match(/\d{3}/g);

            if (ribuan) {
                var separator = sisa ? '.' : '';
                rupiah += separator + ribuan.join('.');
            }

            return 'Rp ' + rupiah;
        }

        // Fungsi untuk menghitung cicilan perbulan
        function hitungCicilan() {
            var jumlahPeminjaman = parseFloat(document.getElementById('jumlah_peminjaman').value.replace('Rp ', '').replace('.', '').replace(',', ''));
            var periodePeminjaman = parseInt(document.getElementById('periode_peminjaman').value);
            var bunga = 0.05; // Bunga 5% (dalam desimal)

            // Perhitungan cicilan perbulan
            var bungaBulanan = bunga / 12;
            var jumlahCicilan = (jumlahPeminjaman * bungaBulanan) / (1 - Math.pow(1 + bungaBulanan, -periodePeminjaman));
            var cicilanPerbulan = jumlahCicilan.toFixed(2);

            // Tampilkan hasil pada elemen dengan id 'monthly_installment' dengan format Rupiah
            document.getElementById('monthly_installment').textContent = formatRupiah(cicilanPerbulan);

            // Tampilkan hasil pada elemen dengan id 'jumlah_peminjaman' dengan format Rupiah
            document.getElementById('formatted_jumlah_peminjaman').textContent = formatRupiah(jumlahPeminjaman);
        }

        // Tambahkan event listener untuk memanggil fungsi hitungCicilan saat input berubah
        document.getElementById('jumlah_peminjaman').addEventListener('input', hitungCicilan);
        document.getElementById('periode_peminjaman').addEventListener('input', hitungCicilan);
    });