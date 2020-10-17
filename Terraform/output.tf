output "instance_ids" {
    value = ["${aws_instance.Jupyther.*.public_ip}"]
}
output "elb_dns_name" {
  value = "${aws_elb.test3.dns_name}"
}
