package com.ronething.course.controller;

import com.alibaba.dubbo.config.annotation.Reference;
import com.ronething.course.dto.CourseDTO;
import com.ronething.course.service.ICourseService;
import com.ronething.thrift.user.dto.UserDTO;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@Controller
@RequestMapping("/course")
public class CourseController {

    @Reference
    private ICourseService courseService;

    @ResponseBody
    @RequestMapping(value = "/courseList", method = RequestMethod.GET)
    public List<CourseDTO> courseList(HttpServletRequest httpServletRequest) {
        UserDTO userDTO = (UserDTO)httpServletRequest.getAttribute("user");
        return courseService.courseList();
    }
}
